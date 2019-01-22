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
    def __init__(self, module=None):
        """初始化"""
        self.skip_module = MyYaml('skip_module').config
        if current_module is None:
            self.current_module = _current_module()
        else:
            self.current_module = module

    @property
    def _is_skip(self):
        """通过.ya中的数据对比当前模块名称是否相等"""
        if isinstance(self.skip_module, dict):
            module = list(self.skip_module.keys())
            reason = list(self.skip_module.values())
            for module in module:
                if module == self.current_module:
                    for reason in reason:
                        return True, reason
        else:
            raise TypeError

    @property
    def is_skip(self):
        """用例执行"""
        skip = self._is_skip[0]
        return skip

    @property
    def is_reason(self):
        """跳过原因"""
        reason = self._is_skip[1]
        return reason

