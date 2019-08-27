from bottle import run, route, template, static_file, error
from config_path.path_file import module_file, read_file
from model.PCParameter import get_network
from model.Yaml import MyConfig

__ip__ = MyConfig('ip').report
__port__ = MyConfig('port').report
__local_ip__ = get_network()['ip地址']
__local_port__ = 20019

IP = __ip__ if __ip__ else __local_ip__
PORT = __port__ if __port__ else __local_port__


@route('/report/<dir_name>/<html_name>')
def report(dir_name, html_name):
    path = read_file(f'report/{dir_name}', html_name)
    return template(path)


@route('/my_static/<filename>')
def my_static_file(filename):
    return static_file(filename, root='../package/report/static')


@error(500)
def error_500(error):
    path = module_file('package/report', 'tpl', 'is_500_tpl.html')
    return template(path, url=IP, port=PORT,
                    local_url=__local_ip__, local_port=__local_port__)


@error(404)
def error_404(error):
    path = module_file('package/report', 'tpl', 'is_404_tpl.html')
    return template(path, url=IP, port=PORT,
                    local_url=__local_ip__, local_port=__local_port__)


if __name__ == '__main__':
    run(host=__local_ip__, port=__local_port__)

