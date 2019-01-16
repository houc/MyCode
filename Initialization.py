import os
import re
import operator

from model.Yaml import MyYaml
from model.ImportTemplate import CURRENCY_PY, CASE_CONTENT, CASE_NAME
from model.PrintColor import RED_BIG
from model.MyException import CreateFileError, FUN_NAME
from model.TimeConversion import standard_time
from model.Logs import Logger
from config_path.path_file import read_file, module_file, PATH


class CreateModule(object):
    """
    该模块主要用于生成测试用例

    Args: 根据Parameter.yaml中的用例，执行该模块，则会自动依Parameter.yaml生成到对应的模块中
    """
    def __init__(self):
        """初始化"""
        self.all_param = MyYaml().parameter_ui
        self.log = Logger()
        self.time = standard_time()
        self.path = os.path.realpath(__file__)
        self.file_path = MyYaml('project_name').excel_parameter
        self.paths = 'IsEDP'
        self.init = '__init__.py'
        self.currency_py = 'currency.py'
        self.currency_ya = 'currency.yaml'
        self.encoding = 'utf-8'

    def _module(self, modules):
        """模块是否存在"""
        try:
            path = read_file(self.paths, modules)
            if not os.path.exists(path):
                os.mkdir(path)
                return modules
            else:
                return modules
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _other_py(self, modules):
        """模块存在后检查__init__.py, currency.py, currency.ya是否存在,当currency.py存在时加入默认数据"""
        module = self._module(modules)
        global path
        if module:
            init_path = module_file(module, self.init)
            currency_py_path = module_file(module, self.currency_py)
            currency_ya_path = module_file(module, self.currency_ya)
            path_list = [init_path, currency_py_path, currency_ya_path]
            try:
                for path in path_list:
                    if not os.path.exists(path):
                        with open(path, 'wt'):
                            pass
                        if self.currency_py in path:
                            with open(path, 'wt', encoding=self.encoding) as f:
                                f.write(CURRENCY_PY)
            except Exception as exc:
                self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _handle_case_data(self, values):
        """处理用例下的数据"""
        case_info = {}
        data = []
        if data:
            data.clear()
        if values:
            case_info["className"] = values.get("className")
            data.append(self._write_case(case_info))
            case_name = [list(case.keys()) for case in values.get("funName")][0]
            for name in case_name:
                for fun in values.get("funName"):
                    fun[name]["caseName"] = name
                    data.append(self._write_case(fun[name], switch=False))
            return data

    def _case_py(self, modules, py, write_one=None):
        """检查用例是否存在,并创建用例中的方法"""
        try:
            case_conversion = py + '.py' if '_st' in py else py + '_st.py'
            case_path = module_file(modules, case_conversion)
            if not os.path.exists(case_path):
                content = self._handle_case_data(write_one[py])
                with open(case_path, 'wt', encoding=self.encoding) as f:
                    f.writelines(content)
            else:
                content = self._handle_case_data(write_one[py])
                with open(case_path, 'rt', encoding=self.encoding) as f:
                    py_read = f.read()
                content = self._conversion_exists(py_read, content)
                if content:
                    with open(case_path, 'wt', encoding=self.encoding) as f:
                        f.writelines(content)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _EXCEPTIONS(self, name, time, reason):
        """异常函数"""
        content = CreateFileError(name, time, reason)
        self.log.logging_debug(content)
        print(RED_BIG, content)
        return False

    def _conversion_exists(self, py_content, ya_content):
        """当用例名称相同时，处理数据判断"""
        case_py = []
        case_ya = []
        try:
            test_name = re.findall('def test_.*?:', py_content)
            [case_py.append(case) for case in test_name]
            for b in ya_content:
                test_name = re.findall('def test_.*?:', b)
                if test_name:
                    for c in test_name:
                        case_ya.append(c)
            assert_list = operator.eq(case_ya, case_py)
            if not assert_list:
                return self._exists_write(case_py, case_ya, py_content, ya_content)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _exists_write(self, case_py, case_ya, py_content, ya_content):
        """处理py中存在的数据进行合并，以py中的数据为基础进行合并至ya中的数据"""
        try:
            case_data = []
            not_eq = [eq for eq in case_ya if not eq in case_py]
            if not_eq:
                case_data.append(py_content)
                case_data.extend(ya_content[1:])
                return self._remove_duplicate(case_data)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _remove_duplicate(self, data):
        """移除重复数据"""
        first_part_storage = []
        defines_case = []
        is_data = [storage.splitlines() for storage in data]
        class_name = [name for name in is_data[0] if name.startswith('class ')][0]
        for first in is_data[0]:
            if class_name in first:
                first_part_storage.append(class_name)
                break
            else:
                first_part_storage.append(first)
        [is_data[0].remove(ines) for ines in first_part_storage]
        for second in range(len(is_data)):
            if second == 0:
                pass
            else:
                defines_case.extend(is_data[second])
        first_part_storage.extend(defines_case)
        return self._line_feed(first_part_storage)

    @staticmethod
    def _line_feed(data):
        """处理换行的问题"""
        is_text = []
        for text in data:
            if not text:
                is_text.append('\n')
            else:
                is_text.append(text + '\n')
        return is_text

    def _case_data_handle(self, modules):
        """用例中的数据处理"""
        case_info = {}
        module = self._module(modules)
        try:
            for value in self.all_param[module]:
                keys = list(value.keys())[0]
                del value[keys]
                case_info[keys] = value
            keys = list(case_info.keys())
            for module in keys:
                self._case_py(modules, module, case_info)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _write_case(self, values, switch=True):
        """写入测试用例"""
        try:
            global elements, case_from
            if switch:
                class_name = values.get("className")
                case_from = class_name + 'Modules'
                case_execute = CASE_CONTENT.format(case_from, class_name)
                return case_execute
            else:
                case_name = values.get("caseName")
                case_doc = values.get("Scene")
                case_level = values.get("Level")
                case_author = values.get("Author")
                case_assert = values.get("Asserts")
                if 'test_' in case_name:
                    elements = self._spilt(case_name, 'case_name')
                if case_doc is None:
                    case_doc = 'None'
                else:
                    if ' ' in case_doc:
                        case_doc = self._spilt(case_doc, 'case_doc')
                case_execute = CASE_NAME.format(case_name, case_doc,'{!r}'.format(case_level),
                                                case_author, case_from, self._spilt(case_name, 'case_name'),
                                                self._spilt(case_assert, 'case_assert'))
                return case_execute
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    @staticmethod
    def _spilt(values, switch):
        """替换和切片"""
        if switch == 'case_name':
            is_split = str(values).split('_')[1]
            return is_split
        elif switch == 'case_doc':
            is_replace = str(values).replace(' ', '\n{}'.format(' ' * 8))
            return is_replace
        elif switch == 'case_assert':
            if '{}' in values:
                is_assert = '{!r}'.format(values) + '.format()'
                return is_assert
            else:
                is_assert = '{!r}'.format(values)
                return is_assert

    @property
    def execute_case(self):
        """处理执行用例"""
        try:
            module = list(self.all_param.keys())
            for run in module:
                self._other_py(run)
                self._case_data_handle(run)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)
        finally:
            return

    def _get_package(self):
        """
        获取包名

        :return 包名以列表形式返回
        """
        path = PATH('.') + '/' + self.file_path
        package = [name for name in os.listdir(path) if '.' not in name ][:-1]
        return package

    def __del__(self):
        """删除不存在的module"""
        module = list(self.all_param.keys())
        package = self._get_package()
        [package.remove(modules) for modules in module if modules in package]
        path = [PATH('.') + '/' + self.file_path + '/' + package_path for package_path in package]
        [os.remove(remove) for remove in path]


if __name__ == '__main__':
    RUN = CreateModule().execute_case
