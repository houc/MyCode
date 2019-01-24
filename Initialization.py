import os
import re
import operator
import shutil

from model.Yaml import MyYaml
from model.ImportTemplate import CURRENCY_PY, CASE_CONTENT, CASE_NAME, XPATH, CSS
from model.PrintColor import RED_BIG
from model.MyException import CreateFileError, FUN_NAME
from model.TimeConversion import standard_time
from model.Logs import Logger
from config_path.path_file import read_file, module_file, PATH


class CreateModule(object):
    """
    该模块主要用于生成测试用例，当ya文件中增加一条用例后，会自动增加载到对应的*_st.py模块下，并且不会去覆盖原*_st.py下的内容！

    Usage:
        common.yaml，文件写法:

            SCRM:    # 项目名称
              login: # 模块名称
                - ValidateLogon: # 用例py
                  url: /user/login # 类通用url，如果此项为填写，自动调用用例下的url，反之调用此处url
                  className: TestLogin # 类名称
                  funName: # 键
                  - test_accountError: {  # 用例名称
                    url: ,  # 用例下的url
                    author: 后超, # 该用例作者
                    level: 低,   # 用例等级
                    scene: '验证错误的用户名登录:
                            1、用户名输入框输入:88888
                            2、密码输入框输入:3333
                            3、点击【登录】',  # 用例场景，（用例步骤或者验证什么结果）
                    element: ['客户管理*/../div[1]', '新建客户*!!send#15928564313', '你好吗*/..!!click', ],
                                # 用例下需要调用的元素名称，定位。目前只支持xpath定位,
                                "你好吗*/..!!click"
                                # 定位文字名称；“*”隔开后面为路径；“!!”隔开后面为执行的方式！

                    get_asserts: ['小同学*'], # 获取预期结果方法，目前只支持xpath定位
                    asserts: '0'  # 预期结果
                  }
                    # 此处用例作为类下多条用例，
                    test_accountLong: {
                    url: ,
                    author: 后超,
                    level: 高,
                    scene: ,
                    element: {},
                    get_asserts: '',
                    asserts: '',
                    }

    """
    def __init__(self):
        """初始化"""
        self.all_param = MyYaml().parameter_ui
        self.log = Logger()
        self.time = standard_time()
        self.path = os.path.realpath(__file__)
        self.file_path = MyYaml('project_name').excel_parameter
        self.paths = self.file_path
        self.init = '__init__.py'
        self.currency_py = 'currency.py'
        self.currency_ya = 'currency.yaml'
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

    def _handle_case_data(self, values: dict):
        """处理用例下的数据"""
        case_info = {}
        data = []
        if data:
            data.clear()
        if values:
            case_info["className"] = values.get("className")
            case_info["url"] = values.get("url")
            data.append(self._write_case(case_info))
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

    def _write_case(self, values: dict, switch=True):
        """写入测试用例"""
        try:
            global elements, case_from, url, case_url
            if switch:
                url = values.get("url")
                class_name = values.get("className")
                # case_from = class_name + 'Modules'
                # case_execute = CASE_CONTENT.format(case_from, class_name)
                case_execute = CASE_CONTENT.format(class_name)
                return case_execute
            else:
                case_name = values.get("caseName")
                case_doc = values.get("scene")
                case_level = values.get("level")
                case_author = values.get("author")
                case_assert = values.get("asserts")
                case_url = values.get("url")
                case_element = values.get("element")
                get_case_assert = values.get("get_asserts")
                HANDLE = self._xpath_css_judge(case_element, get_case_assert)
                if 'test_' in case_name:
                    elements = self._spilt(case_name, 'case_name')
                if case_doc is None:
                    case_doc = '{!r}'.format(None)
                if case_assert is None:
                    case_assert = '{!r}'.format(None)
                if not case_url:
                    if not url:
                        case_url = case_url
                    else:
                        case_url = url
                if ' ' in case_doc:
                    case_doc = self._spilt(case_doc, 'case_doc')
                if HANDLE:
                    case_execute = HANDLE.format(case_name, case_doc, '{!r}'.format(case_level), '{!r}'.
                                                format(case_author), case_url, case_assert)
                    return case_execute
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _element_xpath_handle(self, element: str):
        """xpath元素处理"""
        try:
            if isinstance(element, str):
                param_event = XPATH.format(element.split("#")[0] + '"@ "%s') % \
                              element.split("#")[1] if 'send' in element else XPATH.format(element)
                return param_event.strip()
        except Exception as exc:
            self._EXCEPTIONS(FUN_NAME(self.path), self.time, exc)

    def _element_css_handle(self, element: str):
        """css元素处理"""
        if isinstance(element, str):
            param_event = CSS.format(element.split("!!")[0] + '"@"%s') % \
                          element.split("!!")[1] if 'send' in element else CSS.format(element)
            return param_event.strip()

    def _xpath_css_judge(self, element: list, param: list):
        """判断元素包含xpath或者是css，即分开传递参数"""
        try:
            elements = []
            for attribute in element:
                if 'XPATH:' in attribute:
                    elements.append(self._element_xpath_handle(attribute.split("XPATH:")[1]))
                elif 'CSS:' in attribute:
                    elements.append(self._element_css_handle(attribute.split("CSS:")[1]))
            merge = str(elements)[1:-1].replace("'", "").replace(",", "\n           ").replace("@", ",")
            print(CASE_NAME % (merge,''))
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
        [shutil.rmtree(remove) for remove in path]  # 不管目录是否为空，都将目录删除


if __name__ == '__main__':
    RUN = CreateModule().execute_case
