import requests
import random

from model.Yaml import MyYaml
from IsEDP.InterfaceLogin import GetToken
from model.MyException import RequestsError, FUN_NAME
from config_path.path_file import UP_FILE_NAME

ACCOUNT = MyYaml('account').config
PASSWORD = MyYaml('password').config

def read_public(keys, line):
    """读取public.yaml中的数据"""
    _data = []
    read = MyYaml(UP_FILE_NAME).ModulePublic[keys]
    for i in read:
        _data.append(i['url'])
        _data.append(i['bar'])
    return _data[line]


class _Login(GetToken):
    def __init__(self):
        """初始化"""
        super(_Login, self).__init__()
        self.token = self.read_tokens()

class InterfaceTest(_Login):
    def modify_error(self):
        """通过接口把用户修改成错误的信息"""
        user_id = self._get_user_id()
        role_id = self._get_role_id()
        if user_id:
            if role_id:
                url = MyYaml('EDP_Interface').base_url + read_public('edit_user', 0)
                random_count = ''.join(str(i) for i in random.sample(range(1, 9), 8))
                data = read_public('edit_user', 1)
                data['id'] = user_id[0]
                data['roleId'] = role_id[0]
                data['loginName'] = 'TESTS'
                data['idCard'] = random_count + '26' + random_count
                data['phone'] = '1995027810'
                r = requests.post(url, headers=self.token, data=data, stream=True)
                if r.json().get('code') == 0:
                    return True
                else:
                    raise RequestsError(FUN_NAME(), r.json())

    def modify_correct(self):
        """修改成正确的用户名"""
        user_id = self._get_user_id()
        role_id = self._get_role_id()
        if user_id:
            if role_id:
                url = MyYaml('EDP_Interface').base_url + read_public('edit_user', 0)
                random_count = ''.join(str(i) for i in random.sample(range(1, 9), 8))
                data = read_public('edit_user', 1)
                data['id'] = user_id[0]
                data['roleId'] = role_id[0]
                data['loginName'] = 'TESTS'
                data['idCard'] = random_count + '26' + random_count
                data['phone'] = '19950278100'
                r = requests.post(url, headers=self.token, data=data, stream=True)
                if r.json().get('code') == 0:
                    return True
                else:
                    raise RequestsError(FUN_NAME(), r.json())

    def del_user(self):
        """删除用户"""
        user_id = self._get_user_id()
        if user_id:
            url = MyYaml('EDP_Interface').base_url + read_public('del_user', 0)
            data = read_public('del_user', 1)
            data['id'] = user_id[0]
            r = requests.post(url, headers=self.token, data=data, stream=True)
            if r.json().get('code') == 0:
                return True
            else:
                raise RequestsError(FUN_NAME(), r.json())

    def _get_user_id(self):
        """获取用户id"""
        _data = []
        url = MyYaml('EDP_Interface').base_url + read_public('get_user', 0)
        r = requests.get(url, headers=self.token)
        if r.json().get('code') == 0:
            model = r.json().get('model')
            if model:
                for i in model.get('data'):
                    if 'TESTS' == str(i['loginName']):
                        _data.append(i['id'])
            else:
                add_user = self._add_user()
                if add_user:
                    return self._get_user_id()
            if _data:
                return _data
            else:
                add_user = self._add_user()
                if add_user:
                    return self._get_user_id()
        else:
            raise RequestsError(FUN_NAME(), r.json())

    def _add_user(self):
        """添加用户"""
        role_id = self._get_role_id()
        if role_id:
            random_count = ''.join(str(i) for i in random.sample(range(1, 9), 8))
            url = MyYaml('EDP_Interface').base_url + read_public('add_user', 0)
            data = read_public('add_user', 1)
            data['roleId'] = role_id[0]
            data['loginName'] = 'TESTS'
            data['idCard'] = random_count + random_count + '57'
            r = requests.post(url, headers=self.token, data=data, stream=True)
            if r.json().get('code') == 0:
                return True
            else:
                raise RequestsError(FUN_NAME(), r.json())

    def _get_role_id(self):
        """获取角色id"""
        _data = []
        url = MyYaml('EDP_Interface').base_url + read_public('get_role', 0)
        r = requests.get(url, headers=self.token, stream=True)
        if r.json().get('code') == 0:
            role_id = r.json().get('model').get('data')
            if role_id:
                for i in role_id:
                    if '测试角色' in str(i['name']):
                        _data.append(i['id'])
            else:
                add_role = self._add_role()
                if add_role:
                    return self._get_role_id()
            if _data:
                return _data
            else:
                add_role = self._add_role()
                if add_role:
                    return self._get_role_id()
        else:
            raise RequestsError(FUN_NAME(), r.json())

    def _add_role(self):
        """添加角色"""
        random_count = ''.join(str(i) for i in random.sample(range(1, 9), 4))
        url = MyYaml('EDP_Interface').base_url + read_public('add_role', 0)
        data = read_public('add_role', 1)
        data['name'] = '测试角色' + random_count
        r = requests.post(url, headers=self.token, data=data, stream=True)
        if r.json().get('code') == 0:
            return True
        else:
            raise RequestsError(FUN_NAME(), r.json())


if __name__ == '__main__':
    read_public('add_role', 0)
