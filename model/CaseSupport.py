import functools
import time

from model.Yaml import MyConfig

__skip_status = True


def test_re_runner(set_up, refresh=False):
    re_running_count = MyConfig('re_run_count').config
    except_wait_time = MyConfig('re_sleep').config

    def decorator(method):
        @functools.wraps(method)
        def execute_case(*args, **kwargs):
            for k in range(re_running_count):
                try:
                    execute = method(*args, **kwargs)
                    return execute
                except SyntaxError: raise
                except MemoryError: raise
                except KeyError: raise
                except WindowsError: raise
                except Exception:
                    driver = set_up(*args, **kwargs)
                    if (k + 1) == re_running_count: raise
                    else:
                        time.sleep(except_wait_time)
                        if refresh: driver.refresh()
        return execute_case
    return decorator

