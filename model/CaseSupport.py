import functools
import unittest
import time
import queue
import sys
import warnings
import re

from . Yaml import MyConfig
from . MyDB import MyDB
from unittest.suite import _isnotsuite
from unittest.suite import TestSuite
from unittest.runner import _WritelnDecorator
from unittest.result import TestResult
from unittest.signals import registerResult
from selenium.common import exceptions as EX
from selenium.webdriver.chrome.webdriver import WebDriver

__Skip_Status = True
__Refresh_Url = MyConfig('new_backstage').base_url
__Re_Runner_Test_Count = MyConfig('re_run_count').config
__Wait_Timer = MyConfig('re_sleep').config

# 此模块用于执行测试用例所封装的一系列方法


def test_re_runner(set_up, refresh=False, refresh_url=None, wait_time=None, retry_count=None):
    if retry_count is None:
        retry_count = __Re_Runner_Test_Count
    if wait_time is None:
        wait_time = __Wait_Timer
    if refresh_url is None:
        refresh_url = __Refresh_Url

    def decorator(method):
        @functools.wraps(method)
        def execute_case(*args, **kwargs):
            for count in range(retry_count):
                try:
                    execute = method(*args, **kwargs)
                    return execute
                except (AssertionError, TimeoutError,
                        EX.NoSuchElementException, EX.TimeoutException):
                    driver = set_up(*args, **kwargs)
                    if (count + 1) == retry_count:
                        raise
                    else:
                        if isinstance(driver, WebDriver):
                            time.sleep(wait_time)
                            driver.get(refresh_url)
                            if refresh: driver.refresh()
        return execute_case
    return decorator


def case_self_monitor(case_name=None):
    def decorator(test_case):
        @functools.wraps(test_case)
        def monitors_case(self):
            if test_case.__name__ == case_name:
                raise NameError('用例名不可为当前用例名...')
            failures = [fail[0]._testMethodName for fail in self._outcome.result.failures]
            errors = [error[0]._testMethodName for error in self._outcome.result.errors]
            expected = [expect[0]._testMethodName for expect in self._outcome.result.expectedFailures]
            skipp = [skip[0]._testMethodName for skip in self._outcome.result.skipped]
            total_case = failures + errors + expected + skipp
            if case_name not in total_case:
                def get_method(class_name):
                    for dirt in dir(class_name):
                        if not dirt.startswith('test'):
                            continue
                        test_func = getattr(class_name, dirt)
                        if callable(test_func) and case_name == dirt:
                            return test_func
                tests = get_method(self.__class__)
            elif case_name in failures:
                tests = unittest.skip(f'该用例被上一级{case_name !r}因失败而跳过!')(test_case)
            elif case_name in errors:
                tests = unittest.skip(f'该用例被上一级{case_name !r}因错误而跳过!')(test_case)
            elif case_name in expected:
                tests = unittest.skip(f'该用例被上一级{case_name !r}因预期失败而跳过!')(test_case)
            elif case_name in skipp:
                tests = unittest.skip(f'该用例被上一级{case_name !r}因跳过而跳过!')(test_case)
            else:
                tests = test_case
            print(tests)
            return tests(self)
        return monitors_case
    return decorator


class _Result(TestResult):

    separator1 = '=' * 175
    separator2 = '-' * 175

    def __init__(self, verbosity=True, stream=None):
        super(_Result, self).__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = _WritelnDecorator(stream)
        self.verbosity = verbosity
        self.skip_count = 0
        self.error_count = 0
        self.fail_count = 0
        self.success_count = 0

    @staticmethod
    def _data_update_in_to_my_db(excepts=None, *, case_name, status):
        update = "case_error_reason='%s', case_status='%s'" % (excepts, status)
        base_value = "case_name='%s'" % case_name
        if status in ('成功', '意外成功'): update = "case_status='%s', case_img='%s'" % (status, excepts)
        MyDB().update_db(row_name_value=update, sign_action=base_value)

    def _get_exception(self, errors, status):
        for test, error in errors:
            self._data_update_in_to_my_db(excepts=self.str_conversion(error),
                                          case_name=test._testMethodName,
                                          status=status)

    @staticmethod
    def str_conversion(values: str):
        return re.sub("'", "`", str(values)).replace('\\', '/').replace('"', "`").replace('%', '//')

    def addSkip(self, test, reason):
        TestResult.addSkip(self, test, reason)
        self._skip_data_handle(test, reason)
        if self.verbosity:
            self.stream.write('s')
            self.stream.flush()
        else:
            self.stream.writeln(f"skipped: {reason}")
        self.skip_count += 1

    def _skip_data_handle(self, test, reason):
        catalog = test.__module__ + '.' + test.__class__.__name__
        reasoned = self.str_conversion(reason)
        MyDB().insert_data(case_catalog=catalog, case_status='跳过',
                           case_error_reason=f'跳过原因: {reasoned}',
                           case_name=test._testMethodName)

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
        self._get_exception(self.errors, '错误')
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
        self._get_exception(errors=self.failures, status='失败')
        self.fail_count += 1

    def printErrors(self):
        self.stream.writeln()
        self._print_error_list('ERROR', self.errors)
        self._print_error_list('FAIL', self.failures)
        self._print_error_list('ExpectedFailures', self.expectedFailures)

    def _print_error_list(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s" % (flavour, str(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln("%s" % err)

    def addExpectedFailure(self, test, err):
        TestResult.addExpectedFailure(self, test, err)
        if not self.verbosity:
            self.stream.writeln("expected failure")
        else:
            self.stream.write("x")
            self.stream.flush()
        self._get_exception(errors=self.expectedFailures, status='预期失败')

    def addUnexpectedSuccess(self, test):
        super(_Result, self).addUnexpectedSuccess(test)
        if not self.verbosity:
            self.stream.writeln("unexpected success")
        else:
            self.stream.write("u")
            self.stream.flush()
        self._data_update_in_to_my_db(case_name=test._testMethodName,
                                      status='意外成功')

    def addSuccess(self, test):
        super(_Result, self).addSuccess(test)
        if not self.verbosity:
            self.stream.writeln("ok")
        else:
            self.stream.write('.')
            self.stream.flush()
        self._data_update_in_to_my_db(case_name=test._testMethodName,
                                      status='成功')
        self.success_count += 1


class TestRunning(TestSuite):

    def __init__(self, sequential_execution=False, verbosity=True,
                 stream=None):
        TestSuite.__init__(self)
        self.sequential_execution = sequential_execution
        self.verbosity = verbosity
        self.stream = stream

    def _result(self):
        return _Result(verbosity=self.verbosity, stream=self.stream)

    def _execute_case(self, tmp_list, result):
        top_level = False
        if not getattr(result, '_testRunEntered', False):
            result._testRunEntered = top_level = True
        for test in tmp_list:
            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__
                if (getattr(test.__class__, '_classSetupFailed', False) or
                        getattr(result, '_moduleSetUpFailed', False)):
                    continue
            test(result)
        if top_level:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False

    def run(self, test, debug=False):
        result = self._result()
        registerResult(result)
        with warnings.catch_warnings():
            start_time = time.time()
            start_test_run = getattr(result, 'startTestRun', None)
            if start_test_run is not None:
                start_test_run()
            try:
                if self.sequential_execution:
                    self._thead_execute(test, result)
                else:
                    self._execute_case(test, result)
            finally:
                stop_test_run = getattr(result, 'stopTestRun', None)
                if stop_test_run is not None:
                    stop_test_run()
            stop_time = time.time()
        time_taken = stop_time - start_time
        result.printErrors()
        if hasattr(result, 'separator2'):
            result.stream.writeln(result.separator2)
        run = result.testsRun
        result.stream.writeln("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", time_taken))
        result.stream.writeln()
        expected_fails = unexpected_successes = 0
        try:
            results = map(len, (result.expectedFailures,
                                result.unexpectedSuccesses))
        except AttributeError:
            pass
        else:
            expected_fails, unexpected_successes = results
        infos = []
        if not result.wasSuccessful():
            result.stream.write("FAILED")
            failed, errored = result.fail_count, result.error_count
            if failed:
                infos.append("failures=%d" % failed)
            if errored:
                infos.append("errors=%d" % errored)
        else:
            result.stream.write("OK")
        if result.skip_count:
            infos.append("skipped=%d" % result.skip_count)
        if expected_fails:
            infos.append("expected failures=%d" % expected_fails)
        if unexpected_successes:
            infos.append("unexpected successes=%d" % unexpected_successes)
        if result.success_count:
            infos.append('successes=%d' % result.success_count)
        if infos:
            result.stream.writeln(" (%s)" % (", ".join(infos)))
            result.stream.writeln('\n')
        else:
            result.stream.writeln()
        return result

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
            self._execute_case(tmp_list, result)
