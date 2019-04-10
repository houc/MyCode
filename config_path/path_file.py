import os

def _up_file_name():
    """获取当前文件上级文件名称"""
    return os.path.realpath('.').split('\\')[-1]

def _ups_file_name():
    """获取当前文件上级的上级文件名称"""
    return os.path.realpath('.').split('\\')[-2]

def _current_path(path):
    """当前路径"""
    return os.path.realpath(path)

UP_FILE_NAME = _up_file_name()
UPS_FILE_NAME = _ups_file_name()
PATH = _current_path

def read_file(ups=UPS_FILE_NAME, up=UP_FILE_NAME):
    """获取下级目录"""
    dir_file = os.path.dirname(os.path.dirname(__file__))
    dir_file = dir_file + '/{}/{}'.format(ups, up)
    return dir_file

def module_file(pro, ups=UPS_FILE_NAME, up=UP_FILE_NAME):
    """功能模块路径"""
    dir_file = os.path.dirname(os.path.dirname(__file__))
    dir_file = dir_file + '/{}/{}/{}'.format(pro, ups, up)
    return dir_file

def one_level_catalog(catalog):
    """auto_ui目录下"""
    return os.path.realpath('..' + '/' + catalog)

def module_low(directory_name):
    """UI下的目录名称"""
    return os.path.realpath('.' + '/' + directory_name)

if __name__ == '__main__':
    print(read_file())

