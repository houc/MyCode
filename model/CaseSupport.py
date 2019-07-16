import functools
import time
import queue
import sys

from model.Yaml import MyConfig
from model.MyDB import MyDB
from unittest.suite import _isnotsuite
from unittest.suite import TestSuite
from unittest.runner import _WritelnDecorator
from unittest.result import TestResult

__Skip_Status = True
__Refresh_Url = MyConfig('url').base_url


def test_re_runner(set_up, refresh=False, refresh_url=None):
    re_running_count = MyConfig('re_run_count').config
    except_wait_time = MyConfig('re_sleep').config
    if refresh_url is None:
        refresh_url = __Refresh_Url

    def decorator(method):
        @functools.wraps(method)
        def execute_case(*args, **kwargs):
            for k in range(re_running_count):
                try:
                    execute = method(*args, **kwargs)
                    return execute
                except SyntaxError:
                    raise
                except MemoryError:
                    raise
                except KeyError:
                    raise
                except WindowsError:
                    raise
                except Exception:
                    driver = set_up(*args, **kwargs)
                    if (k + 1) == re_running_count:
                        raise
                    else:
                        time.sleep(except_wait_time)
                        if refresh:
                            driver.get(refresh_url)
                            driver.refresh()
        return execute_case
    return decorator


class _Result(TestResult):

    separator1 = '=' * 160
    separator2 = '-' * 160

    def __init__(self, verbosity=True, stream=None):
        super(_Result, self).__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = _WritelnDecorator(stream)
        self.verbosity = verbosity
        self.skip_count = 0
        self.error_count = 0
        self.fail_count = 0

    def addSkip(self, test, reason):
        TestResult.addSkip(self, test, reason)
        self._skip_data_handle(test, reason)
        if self.verbosity:
            self.stream.write('s')
            self.stream.flush()
        else:
            self.stream.writeln(f"skipped: {reason}")
        self.skip_count += 1

    @staticmethod
    def _skip_data_handle(test, reason):
        catalog = test.__module__ + '.' + test.__class__.__name__
        name = str(test).split(' (')[0]
        MyDB().insert_data(ids=catalog, level=None,
                           module=None, name=name, remark=None,
                           wait_time=None, status='跳过', url=None,
                           insert_time=None, img=None, error_reason=f'跳过原因: {reason}',
                           author=None, results_value=None)

    def startTest(self, test):
        TestResult.startTest(self, test)
        if not self.verbosity:
            self.stream.write(str(test))
            self.stream.write(' ... ')
            self.stream.flush()

    def addError(self, test, err):
        TestResult.addError(self, test, err)
        if self.verbosity:
            self.stream.write('E')
            self.stream.flush()
        else:
            self.stream.writeln("ERROR")
        self.error_count += 1

    def stopTest(self, test):
        TestResult.stopTest(self, test)

    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
        if self.verbosity:
            self.stream.write('F')
            self.stream.flush()
        else:
            self.stream.writeln("fail")
        self.fail_count += 1

    def printErrors(self):
        self.stream.writeln()
        self._printErrorList('ERROR', self.errors)
        self._printErrorList('FAIL', self.failures)

    def _printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s" % (flavour, str(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln("%s" % err)


class TestRunning(TestSuite):

    __class_result = _Result

    def __init__(self, sequential_execution=False, verbosity=True,
                 stream=None):
        super(TestRunning, self).__init__(self)
        self.sequential_execution = sequential_execution
        self.verbosity = verbosity
        self.stream = stream

    def _result(self):
        return self.__class_result(verbosity=self.verbosity, stream=self.stream)

    def _execute_case(self, tmp_list, result):
        for test_case in tmp_list:
            if _isnotsuite(test_case):
                self._tearDownPreviousClass(test_case, result)
                self._handleModuleFixture(test_case, result)
                self._handleClassSetUp(test_case, result)
                result._previousTestClass = test_case.__class__
                if (getattr(test_case.__class__, '_classSetupFailed', False) or
                        getattr(result, '_moduleSetUpFailed', False)):
                    continue
            test_case(result)
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)

    def run(self, suite, debug=False):
        result = self._result()
        start_time = time.time()
        if self.sequential_execution:
            self._thead_execute(suite, result)
        else:
            self._execute_case(suite, result)
        ends_time = time.time()
        s = '{:.3f}s '.format(ends_time - start_time)
        result.printErrors()
        result.stream.writeln()
        result.stream.write(f'run {result.testsRun} is {s}'
                            f'(errors: {result.error_count}; '
                            f'failed: {result.fail_count}; '
                            f'skipped: {result.skip_count};)')
        result.stream.writeln()
        result.stream.flush()

    def _thead_execute(self, suite, result):
        test_case_queue = queue.LifoQueue()
        L = []
        tmp_key = None
        for test_case in suite:
            tmp_class_name = test_case.__class__
            if tmp_key == tmp_class_name:
                L.append(test_case)
            else:
                tmp_key = tmp_class_name
                if len(L) != 0:
                    test_case_queue.put(L.copy())
                    L.clear()
                L.append(test_case)
        if len(L) != 0:
            test_case_queue.put(L.copy())
        while not test_case_queue.empty():
            tmp_list = test_case_queue.get()
            self._thread_execute_call(tmp_list, result)

    @staticmethod
    def _thread_execute_call(suite, result):
        raise SyntaxError('多线程暂不完善，请使用单线程运行该用例集....')