import os
import shutil
import time

from bottle import template
from datetime import datetime, timedelta
from config_path.path_file import read_file, module_file
from collections import defaultdict
from model.Yaml import MyConfig
from model.TimeConversion import standard_time, compact_time
from model.ImportTemplate import GetTemplateHTML
from model.DriverParameter import browser
from package.pie_link import HTML
from model.Thread import MyThread


class AmilSupport(object):
    def __init__(self, case_data, browser_switch=True, html_name='html_report', encoding='utf-8'):
        """该方法主要用于，邮件发送的一些支持类方法"""
        self.html_name = html_name
        self.encoding = encoding
        self.switch_browser = browser_switch
        self.title = MyConfig('project_name').excel_parameter
        self.science = MyConfig('science').excel_parameter
        MyThread({self._browser_get_html: (case_data, )}).run()

    def _html_handle(self, case_data):
        """
        处理html中的数据
        :param case_data: 传过来的统计数据
        :return: 返回处理后的数据类型
        """
        return HTML % ('100%', '100%', '100%', self.title + '统计简报', self.science,
                       case_data.get('errors'), case_data.get('failures'),
                       case_data.get('skipped'), case_data.get('success'),
                       '55%', '25%', '50%', '30%', '{b}: {@错误数} ({d}%)',
                       '{b}: {@[" + dimension + "]} ({d}%)')

    def _save_as_report(self, case_name):
        """
        此方法主要用于，html存储
        :return: 返回对应的路径
        """
        path = read_file('report', '{}.html'.format(self.html_name))
        html = self._html_handle(case_name)
        with open(path, 'wt', encoding=self.encoding) as f:
            f.writelines(html)
        return path

    def _browser_get_html(self, case_name):
        """
        将请求的html用浏览器请求
        :return: ...
        """
        path = self._save_as_report(case_name)
        img_path = read_file('img', 'html.png')
        driver = browser(switch=self.switch_browser)
        driver.get(path)
        import time
        time.sleep(2)
        driver.save_screenshot(img_path)
        driver.quit()


class MyReport(object):
    def __init__(self):
        self.path = module_file('package/report', 'tpl', 'my_html.tpl')
        self.new_dict = defaultdict(dict)
        self.finish_dict = defaultdict(dict)
        self.save = MyConfig('save').report
        self.server = 'http://{}:{}'.format(MyConfig('ip').report, MyConfig('port').report)
        self.encoding = 'utf8'
        self.skipped = ''
        self.success = ''
        self.error = ''
        self.failed = ''
        self.case_info = ''

    def execute(self, *args, **kwargs):
        conversion_list = self._conversion_list(args)
        case_info = []
        for value in conversion_list:
            if value[6] == '失败':
                html = self._new_dict(value)
                self.failed += html[1]
                case_info.append(html[0])
            elif value[6] == '成功':
                html = self._new_dict(value)
                self.success += html[1]
                case_info.append(html[0])
            elif value[6] == '跳过':
                html = self._new_dict(value)
                self.skipped += html[1]
                case_info.append(html[0])
            elif value[6] == '错误':
                html = self._new_dict(value)
                self.error += html[1]
                case_info.append(html[0])
        self._handle_case_discover(case_info)
        self.finish_dict.update(kwargs)
        html = self._template_conversion_html()
        return self._create_html(html)

    def _create_html(self, html):
        self._del_dir()
        date = standard_time().split(' ')[0]
        path = read_file('report', date)
        if not os.path.exists(path):
            os.mkdir(path)
        path = path + '/{}.html'.format(compact_time())
        with open(path, 'wt', encoding=self.encoding) as f:
            f.write(html)
        if os.path.exists(path):
            return self._path_handle(path)
        else:
            raise OSError('测试报告未能生成！')

    def _path_handle(self, path):
        return '{}/report{}'.format(self.server, path.split('report')[-1])

    def _del_dir(self):
        for time in range(self.save):
            date = (datetime.today() - timedelta(days=time + self.save)).strftime('%Y-%m-%d')
            path = read_file('report', date)
            if os.path.exists(path):
                shutil.rmtree(path)

    def _handle_case_discover(self, case_info):
        for info in case_info:
            self.case_info += info
        self.finish_dict['popUP'] = self.case_info
        self.finish_dict['success_list'] = self.success
        self.finish_dict['skip_list'] = self.skipped
        self.finish_dict['error_list'] = self.error
        self.finish_dict['fail_list'] = self.failed

    def _new_dict(self, value):
        return self._html(catalog=value[0], modules=value[2], level=value[1], method=value[3], address=value[4],
                          scene=value[5], expect=value[7], actual=value[8], finish_time=value[12],
                          status=value[6], use_time=value[9], members=value[11], remark=value[10],
                          id=value[3])

    def _conversion_list(self, args):
        new_list = []
        for info in args:
            for case in info:
                for keys, value in enumerate(case):
                    self.new_dict[keys] = value
                new_list.append(dict(self.new_dict))
        return new_list

    def _html(self, catalog, modules, level, method, address, scene, expect, actual, status, finish_time,
                 use_time, remark, id, members):
        html = GetTemplateHTML(catalog, modules, level, method, address, scene, expect, actual, status, finish_time,
                 use_time, remark, id, members)
        return html.case_info(), html.case_list()

    def _template_conversion_html(self):
        html = template(self.path, popUP=self.finish_dict['popUP'], success_list=self.finish_dict['success_list'],
                        skip_list=self.finish_dict['skip_list'], error_list=self.finish_dict['error_list'],
                        fail_list=self.finish_dict['fail_list'], tool=self.finish_dict['tool'],
                        science=self.finish_dict['science'], version=self.finish_dict['version'],
                        efficiency=self.finish_dict['efficiency'], start_time=self.finish_dict['start_time'],
                        ends_time=self.finish_dict['ends_time'], long_time=self.finish_dict['long_time'],
                        sort_time=self.finish_dict['sort_time'], total_case=self.finish_dict['total_case'],
                        failed_case=self.finish_dict['failed_case'], error_case=self.finish_dict['error_case'],
                        success_case=self.finish_dict['success_case'], skipped_case=self.finish_dict['skipped_case'],
                        fraction=self.finish_dict['fraction'], url=self.server,
                        execute_method=self.finish_dict['execute_method'],
                        execute_time=self.finish_dict['execute_time'],
                        project=self.finish_dict['project'])
        return html.replace('&lt;', '<').replace('&gt;', '>').replace('&#039;', '"').replace('&quot;', '"')


class screenshot(object):
    def __init__(self, url):
        self.path = read_file('img', 'html.png')
        driver = browser(switch=True)
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(2)
        driver.set_window_size(1900, 500)
        driver.save_screenshot(self.path)
        driver.quit()
