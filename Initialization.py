import os

from model.Yaml import MyYaml
from model.ImportTemplate import CURRENCY_PY
from model.PrintColor import RED_BIG
from model.MyException import CreateFileError
from model.TimeConversion import standard_time
from model.Logs import Logger
from config_path.path_file import read_file, module_file


class CreateModule(object):
    def __init__(self):
        """初始化"""
        self.all_param = MyYaml().parameter_ui
        self.log = Logger()
        self.paths = 'IsEDP'
        self.init = '__init__.py'
        self.currency_py = 'currency.py'
        self.currency_yaml = 'currency.yaml'
        self.encoding = 'utf-8'

    @property
    def _module(self):
        """模块是否存在"""
        global route
        module = list(self.all_param.keys())
        try:
            for route in module:
                path = read_file(self.paths, route)
                if not os.path.exists(path):
                    os.mkdir(path)
            else:
                return route
        except Exception as exc:
            content = CreateFileError(route, standard_time(), exc)
            self.log.logging_debug(content)
            print(RED_BIG, content)
            return False

    @property
    def _other_py(self):
        """模块存在后检查__init__.py, currency.py, currency.yaml是否存在,当currency.py存在时加入默认数据"""
        module = self._module
        global path
        if module:
            init_path = module_file(module, self.init)
            currency_py_path = module_file(module, self.currency_py)
            currency_yaml_path = module_file(module, self.currency_yaml)
            path_list = [init_path, currency_py_path, currency_yaml_path]
            try:
                for path in path_list:
                    if not os.path.exists(path):
                        with open(path, 'w'):
                            pass
                        if os.path.exists(path):
                            if self.currency_py in path:
                                with open(path, 'w', encoding=self.encoding) as f:
                                    f.write(CURRENCY_PY)
                else:
                    return path
            except Exception as exc:
                content = CreateFileError(route, standard_time(), exc)
                self.log.logging_debug(content)
                print(RED_BIG, content)
                return False

    @property
    def case_py(self):
        """检查用例是否存在,并创建用例中的方法"""
        module = self._module
        if module:
            class_info = self.all_param[module]
            try:
                for py in class_info:
                    case_conversion = py["module"] + '.py' if '_st' in py["module"] else py["module"] + '_st.py'
                    case_path = module_file(module, case_conversion)
                    if not os.path.exists(case_path):
                        with open(case_path, 'w'):
                            pass
                        if os.path.exists(case_path):
                            with open(case_path, 'w', encoding=self.encoding) as f:
                                pass

            except Exception as exc:
                content = CreateFileError(route, standard_time(), exc)
                self.log.logging_debug(content)
                print(RED_BIG, content)
                return False

    @property
    def _case_data_handle(self):
        """用例中的数据处理"""
        class_info = {}
        case_info = {}
        module = self._module
        try:
            for py in self.all_param[module]:
                for is_class in py["class"]:
                    class_info["class_name"] = is_class["class_name"]
                    class_info["class_doc"] = is_class["class_doc"]
                    for is_case in is_class["case"]:
                        case_info["case_name"] = is_case["case_name"]
                        case_info["case_author"] = is_case["case_author"]
                        case_info["case_scene"] = is_case["case_scene"]
                        case_info["case_elements"] = is_case["case_elements"]
                        case_info["send_param"] = is_case["send_param"]
                        case_info["case_level"] = is_case["case_level"]
                        case_info["case_assert"] = is_case["case_assert"]
            else:
                return case_info, class_info
        except Exception as exc:
            content = CreateFileError(route, standard_time(), exc)
            self.log.logging_debug(content)
            print(RED_BIG, content)
            return False

    @property
    def data_merge(self):
        """将类和用例进行合并合并数据"""
        class_message = self._case_data_handle[1]
        case_message = self._case_data_handle[0]
        merge = dict(case_message, **class_message)
        return merge


print(CreateModule().data_merge)