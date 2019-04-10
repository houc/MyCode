import os
import re
import operator
import shutil

from model.Yaml import MyConfig, MyProject
from model.ImportTemplate import CURRENCY_PY, CASE_CONTENT, CASE_NAME, CURRENCY_YA, PROJECT_COMMON
from model.PrintColor import RED_BIG
from model.MyException import CreateFileError, FUN_NAME
from model.TimeConversion import standard_time
from model.Logs import Logger
from config_path.path_file import read_file, module_file, PATH


class CreateModule(object):
    def __init__(self):
        """初始化"""
        self.log = Logger()
        self.time = standard_time()
        self.path = os.path.realpath(__file__)
        self.file_path = MyConfig('project_name').excel_parameter
        self.all_param = MyProject(self.file_path).parameter_ui
        self.paths = self.file_path
        self.init = '__init__.py'
        self.currency_py = 'currency.py'
        self.currency_ya = 'currency.yaml'
        self.common_ya = 'common.yaml'
        self.common_py = 'common.py'
        self.encoding = 'utf-8'

    def _module(self, modules: classmethod):
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

    def _other_py(self, modules: classmethod):
        """模块存在后检查__init__.py, currency.py, currency.ya是否存在,当currency.py、currency.ya存在时加入默认数据"""
        module = self._module(modules)
        global path
        if module:
            init_path = module_file(self.file_path, module, self.init)
            currency_py_path = module_file(self.file_path, module, self.currency_py)
            currency_ya_path = module_file(self.file_path, module, self.currency_ya)
            path_list = [init_path, currency_py_path, currency_ya_path]
            content = "".join(str(module).title().split("_")) + "Element"
            try:
                for path in path_list:
                    if not os.path.exists(path):
                        with open(path, 'wt'):
                            pass
                        if self.currency_py in path:
                            with open(path, 'wt', encoding=self.encoding) as f:
                                f.write(CURRENCY_PY.format(content) % (content))
                        if self.currency_ya in path:
                            with open(path, 'wt', encoding=self.encoding) as f:
                                f.write(CURRENCY_YA)
            except Exception as exc:
                self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _handle_case_data(self, values: dict, module=None):
        """处理用例下的数据"""
        case_info = {}
        data = []
        if data:
            data.clear()
        if values:
            case_info["className"] = values.get("className")
            case_info["url"] = values.get("url")
            data.append(self._write_case(case_info, module=module))
            case_name = [list(case.keys()) for case in values.get("funName")][0]
            for name in case_name:
                for fun in values.get("funName"):
                    fun[name]["caseName"] = name
                    data.append(self._write_case(fun[name], switch=False))
            return data

    def _case_py(self, modules: classmethod, py: str, write_one=None):
        """检查用例是否存在,并创建用例中的方法"""
        try:
            case_conversion = py + '.py' if '_st' in py else py + '_st.py'
            case_path = module_file(self.file_path, modules, case_conversion)
            if not os.path.exists(case_path):
                content = self._handle_case_data(write_one[py], module=modules)
                with open(case_path, 'wt', encoding=self.encoding) as f:
                    f.writelines(content)
            else:
                content = self._handle_case_data(write_one[py], module=modules)
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

    def _conversion_exists(self, py_content: str, ya_content: list):
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

    def _exists_write(self, case_py: list, case_ya: list, py_content: str, ya_content: list):
        """处理py中存在的数据进行合并，以py中的数据为基础进行合并至ya中的数据"""
        try:
            case_data = []
            not_eq = [eq for eq in case_ya if not eq in case_py]
            if not_eq:
                case_data.append(py_content)
                case_data.extend(ya_content[1:])
                return self._remove_duplicate(case_data, not_eq)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _remove_duplicate(self, data: list, defines: list):
        """移除重复数据"""
        ya_content = []
        content = [storage.splitlines() for storage in data]   # content[0] py中的内容，content[↑]ya中的内容
        for ya in range(len(content)):
            if ya == 0:
                for py in content[ya]:
                    ya_content.append(py)
            else:
                for fun in defines:
                    if fun in str(content[ya]):
                        for text in content[ya]:
                            ya_content.append(text)
        return self._line_feed(ya_content)

    @staticmethod
    def _line_feed(data: list):
        """处理换行的问题"""
        is_text = []
        for text in data:
            if not text:
                is_text.append('\n')
            else:
                is_text.append(text + '\n')
        return is_text

    def _case_data_handle(self, modules: classmethod):
        """用例中的数据处理"""
        case_info = {}
        try:
            for value in self.all_param[modules]:
                keys = list(value.keys())[0]
                del value[keys]
                case_info[keys] = value
            keys = list(case_info.keys())
            for module in keys:
                self._case_py(modules, module, case_info)
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _write_case(self, values: dict, switch=True, module=None):
        """写入测试用例"""
        try:
            global elements, case_from, content
            if switch:
                path = self.file_path + "." + module + ".currency"
                class_name = values.get("className")
                content = ''.join(str(module).title().split("_")) + "Element"
                case_execute = CASE_CONTENT.format(path ,content, class_name)
                return case_execute
            else:
                case_name = values.get("caseName")
                case_doc = values.get("scene")
                if 'test_' in case_name:
                    elements = self._spilt(case_name, 'case_name')
                if case_doc is None:
                    case_doc = '{!r}'.format(None)
                if ' ' in case_doc:
                    case_doc = self._spilt(case_doc, 'case_doc')
                if CASE_NAME:
                    case_execute = CASE_NAME.format(case_name, case_doc, content)
                    return case_execute
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    @staticmethod
    def _spilt(values: str, switch: str):
        """替换和切片"""
        if switch == 'case_name':
            is_split = str(values).split('_')[1]
            return is_split
        if switch == 'case_doc':
            is_replace = str(values).replace(' ', '\n{}'.format(' ' * 8))
            return is_replace
        if switch == 'case_assert':
            if '{}' in values:
                is_assert = '{!r}'.format(values) + '.format()'
                return is_assert
            else:
                is_assert = '{!r}'.format(values)
                return is_assert

    def _project_check(self):
        """用于判断项目目录是否存在，不存在重新创建，项目并生成对应的py"""
        project_path = PATH('.') + '\\' + self.file_path
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            with open(project_path + '\\' + self.common_py, 'wt', encoding=self.encoding) as f:
                f.write(PROJECT_COMMON)
                with open(project_path + '\\' + self.common_ya, 'wt', encoding=self.encoding):
                    with open(project_path + '\\' + self.init, 'wt', encoding=self.encoding):
                        pass

    def execute_case(self):
        """处理执行用例,switch计算用例总计"""
        self._project_check()
        case = self.check_repeat()
        for key, values in self.all_param.items():
            self._other_py(key)
            self._case_data_handle(key)
        import sys
        print('共{}条用例,已全部初始化完毕...'.format(len(case)), file=sys.stderr)

    def check_repeat(self):
        """
        检查common中的用例是否存在重复, 存在重复提示异常！
        :parameter switch 计算用例条数
        :return: 返回所有的case
        """
        case_name = []
        for key, values in self.all_param.items():
            for value in values:
                for value in value['funName']:
                    for key, values in value.items():
                        case_name.append(key)
        if case_name:
            repeat = [val for val in list(set(case_name)) if case_name.count(val) >= 2]
            if repeat:
                import warnings
                warnings.warn('注意-->有重复的用例名称，用例名称:' + ', '.join(repeat))
            return case_name

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
        [shutil.rmtree(remove) for remove in path]  # 不管目录是否为空，都将目录删除


if __name__ == '__main__':
    CreateModule().execute_case()

