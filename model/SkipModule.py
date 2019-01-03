import os
import sys

from model.Yaml import MyYaml

def _current_module():
    """获取当前py名称"""
    name = os.path.basename(sys.argv[0]).split('.')[0]
    return name

def current_module(path):
    """获取当前py名称"""
    name = os.path.basename(path).split('.')[0]
    return name

class Skip(object):
    def __init__(self, current_module=None):
        """初始化"""
        self.skip_module = MyYaml('skip_module').config
        if current_module is None:
            self.current_module = _current_module()
        else:
            self.current_module = current_module

    @property
    def is_skip(self):
        """通过yaml中的数据对比当前模块名称是否相等"""
        if isinstance(self.skip_module, list):
            for module in self.skip_module:
                if module == self.current_module:
                    return True
        else:
            if self.skip_module == self.current_module:
                return True

