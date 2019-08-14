# 该模块主要用于ActionChains的封装继承类
# 可自定义元素在规定时间内运行并检查它们是否存在

__author__ = 'hc'


class GetCurrentUrl(object):
    def __call__(self, driver):
        return driver.current_url

