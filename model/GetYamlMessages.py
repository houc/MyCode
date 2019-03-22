import re

from model.Yaml import MyYaml


class GetConfigMessage(object):
    """用例读取common.yaml文件中的内容"""
    def __init__(self, module="marketing_transformation", class_name="TestMarketingTransformation", case_name="test_up"):
        """
        初始化，读取common中的数据，self.data_messages为对应数据
        :param module: 模块：如 staff_manage
        :param class_name: 类：如：'className': 'TestLogin'
        :param case_name: 用例名称：如：test_accountError
        """
        self.url = MyYaml('SCRM').base_url
        data_messages = {}
        self.all_parm = MyYaml().parameter_ui
        for a in self.all_parm[module]:
            if a["className"] == class_name:
                url = self.url + a['url']
                for b in a["funName"]:
                    value = b[case_name]
                    if value["url"] is not None:
                        url = self.url + value["url"]
                    data_messages["url"] = url
                    data_messages["author"] = value["author"]
                    data_messages["level"] = value["level"]
                    data_messages["asserts"] = value["asserts"]
                    data_messages["scene"] = value["scene"]
        if data_messages:
            self.data_messages = data_messages
        else:
            raise TypeError("data_messages无数据，请检查对应参数是否正确")

    def re(self):
        """返回数据"""
        return self.data_messages

    def param_extract(self, value: str):
        """
        处理场景中存在的{XX}数据，进行转换处理
        :param value: 场景的所有数据
        :return: 返回{}里面的数据
        """
        data = re.findall("{(.*?)}", value)
        if isinstance(data, list) and data:
            return data
        else:
            return False

if __name__ == '__main__':
    H = GetConfigMessage()
    print(H.re())
    # print(H.param_extract(H.re().get("scene")))
