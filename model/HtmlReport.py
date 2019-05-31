import sys
import os
PATH = os.path.dirname(os.path.abspath('.'))
sys.path.append(PATH)

from bottle import run, route, template, static_file, error
from config_path.path_file import module_file, read_file


@route('/report/<dir_name>/<html_name>')
def report(dir_name, html_name):
    path = read_file('report/{}'.format(dir_name) , html_name)
    return template(path)

@route('/my_static/<filename>')
def my_static_file(filename):
    return static_file(filename, root='../package/report/static')

@error(500)
def error_500(error):
    from model.Yaml import MyConfig
    url = 'http://{}:{}'.format(MyConfig('ip').report, MyConfig('port').report)
    path = module_file('package/report', 'tpl', 'is_500_tpl.tpl')
    return template(path, url=url)

@error(404)
def error_404(error):
    from model.Yaml import MyConfig
    url = 'http://{}:{}'.format(MyConfig('ip').report, MyConfig('port').report)
    path = module_file('package/report', 'tpl', 'is_404_tpl.tpl')
    return template(path, url=url)


if __name__ == '__main__':
    from model.Yaml import MyConfig
    ip = MyConfig('ip').report
    port = MyConfig('port').report
    run(host=ip, port=port)
