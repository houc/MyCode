import time
import contextlib
import sys

from unittest import TestCase

class SkipTest(Exception):
    """
    Raise this exception in a test to skip it.

    Usually you can use TestCase.skipTest() or one of the skipping decorators
    instead of raising this directly.
    """

class _ShouldStop(Exception):
    """
    The test should stop.
    """

class _UnexpectedSuccess(Exception):
    """
    The test was supposed to fail, but it didn't!
    """

class _Outcome(object):
    def __init__(self, result=None):
        self.expecting_failure = False
        self.result = result
        self.result_supports_subtests = hasattr(result, "addSubTest")
        self.success = True
        self.skipped = []
        self.expectedFailure = None
        self.errors = []

    @contextlib.contextmanager
    def testPartExecutor(self, test_case, isTest=False):
        old_success = self.success
        self.success = True
        try:
            yield
        except KeyboardInterrupt:
            raise
        except SkipTest as e:
            self.success = False
            self.skipped.append((test_case, str(e)))
        except _ShouldStop:
            pass
        except:
            exc_info = sys.exc_info()
            if self.expecting_failure:
                self.expectedFailure = exc_info
            else:
                self.success = False
                self.errors.append((test_case, exc_info))
            # explicitly break a reference cycle:
            # exc_info -> frame -> exc_info
            exc_info = None
        else:
            if self.result_supports_subtests and self.success:
                self.errors.append((test_case, None))
        finally:
            self.success = self.success and old_success


class ReRun(TestCase):
    """失败或者错误时，重跑用例"""
    def run(self, result=None):
        orig_result = result
        if result is None:
            result = self.defaultTestResult()
            startTestRun = getattr(result, 'startTestRun', None)
            if startTestRun is not None:
                startTestRun()
        result.startTest(self)
        while_case = result.while_case
        while_sleep = result.while_sleep
        testMethod = getattr(self, self._testMethodName)
        if (getattr(self.__class__, "__unittest_skip__", False) or getattr(testMethod, "__unittest_skip__", False)):
            try:
                skip_why = (getattr(self.__class__, '__unittest_skip_why__', '') or getattr(testMethod,
                                                                                            '__unittest_skip_why__',
                                                                                            ''))
                self._addSkip(result, self, skip_why)
            finally:
                result.stopTest(self)
            return
        expecting_failure_method = getattr(testMethod, "__unittest_expecting_failure__", False)
        expecting_failure_class = getattr(self, "__unittest_expecting_failure__", False)
        expecting_failure = expecting_failure_class or expecting_failure_method
        try:
            outcome = _Outcome(result)
            self._outcome = outcome
            with outcome.testPartExecutor(self):
                self.setUp()
            if outcome.success:
                outcome.expecting_failure = expecting_failure
                with outcome.testPartExecutor(self, isTest=True):
                    testMethod()
                outcome.expecting_failure = False
                with outcome.testPartExecutor(self):
                    self.tearDown()
                self.doCleanups()
                for test, reason in outcome.skipped:
                    self._addSkip(result, test, reason)
                if (not outcome.success) and len([error for error in outcome.errors if error[1] is not None]) > 0:
                    if isinstance(while_case, int) and isinstance(while_sleep, int):
                        for i in range(while_case):
                            outcome = _Outcome(result)
                            self._outcome = outcome
                            time.sleep(while_sleep)
                            with outcome.testPartExecutor(self):
                                self.setUp()
                            if outcome.success:
                                outcome.expecting_failure = expecting_failure
                                with outcome.testPartExecutor(self, isTest=True):
                                    testMethod()
                                outcome.expecting_failure = False
                                with outcome.testPartExecutor(self):
                                    self.tearDown()
                                self.doCleanups()
                            if outcome.success:
                                break
                        if outcome.errors:
                            self._feedErrorsToResult(result, outcome.errors)
                    else:
                        raise TypeError('用例错误尝试的参数应为“int”型')
            if outcome.success:
                if expecting_failure:
                    if outcome.expectedFailure:
                        self._addExpectedFailure(result, outcome.expectedFailure)
                    else:
                        self._addUnexpectedSuccess(result)
                else:
                    result.addSuccess(self)
            return result
        finally:
            result.stopTest(self)
            if orig_result is None:
                stopTestRun = getattr(result, 'stopTestRun', None)
                if stopTestRun is not None:
                    stopTestRun()
            # explicitly break reference cycles:
            # outcome.errors -> frame -> outcome -> outcome.errors
            # outcome.expectedFailure -> frame -> outcome -> outcome.expectedFailure
            outcome.errors.clear()
            outcome.expectedFailure = None
            # clear the outcome, no more needed
            self._outcome = None