from bottle import run, route, template, static_file, error
from config_path.path_file import module_file, read_file
from model.PCParameter import get_network
from model.Yaml import MyConfig

PORT = MyConfig('port').report if  MyConfig('ip').report else 2019
IP = MyConfig('ip').report if MyConfig('ip').report else get_network()['ip地址']


@route('/report/<dir_name>/<html_name>')
def report(dir_name, html_name):
    path = read_file('report/{}'.format(dir_name) , html_name)
    return template(path)


@route('/my_static/<filename>')
def my_static_file(filename):
    return static_file(filename, root='../package/report/static')


@error(500)
def error_500(error):
    path = module_file('package/report', 'tpl', 'is_500_tpl.tpl')
    return template(path, url=IP)


@error(404)
def error_404(error):
    path = module_file('package/report', 'tpl', 'is_404_tpl.tpl')
    return template(path, url=IP)


if __name__ == '__main__':
    run(host=IP, port=PORT)
