import os


def read_file(dir,dirName):
    """获取下级目录"""
    dir_file = os.path.dirname(os.path.dirname(__file__))
    dir_file = dir_file + '/{}/{}'.format(dir,dirName)
    return dir_file

if __name__ == '__main__':
    print(read_file('',''))
