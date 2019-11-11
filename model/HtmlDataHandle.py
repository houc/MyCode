import os
import shutil
import time

from bottle import template
from config_path.path_file import read_file, module_file
from collections import defaultdict
from . Yaml import MyConfig
from . HtmlReport import (IP, __local_ip__, __local_port__, PORT)
from . TimeConversion import standard_time, compact_time, return_y_d_m
from . ImportTemplate import GetTemplateHTML
from . DriverParameter import browser
from . CaseSupport import _Result
from . SeleniumElement import OperationElement
from selenium.common.exceptions import TimeoutException


class MyReport(object):
    def __init__(self):
        self.path = module_file('package/report', 'tpl', 'my_html.tpl')
        self.new_dict = defaultdict(dict)
        self.finish_dict = defaultdict(dict)
        self.save = MyConfig('save').report
        self.encoding = 'utf8'
        self.skipped = ''
        self.success = ''
        self.error = ''
        self.failed = ''
        self.failure = ''
        self.unexpected_success = ''
        self.case_info = ''
        self.local_server = f'http://{__local_ip__}:{__local_port__}'
        self.wide_server = f'http://{IP}:{PORT}'

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
            elif value[6] == '意外成功':
                html = self._new_dict(value)
                self.unexpected_success += html[1]
                case_info.append(html[0])
            elif value[6] == '预期失败':
                html = self._new_dict(value)
                self.failure += html[1]
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
        if html:
            with open(path, 'wt', encoding=self.encoding) as w:
                w.write(html)
        else:
            raise IOError('report in html is empty data!')
        if os.path.exists(path):
            with open(path, 'rt', encoding=self.encoding) as r:
                readline = r.readlines()
                if readline:
                    return self._path_handle(path)
                else:
                    raise IOError('无法访问网页形式测试报告，因为测试报告中数据为空！')
        else:
            raise IOError('测试报告未能生成！')

    def _path_handle(self, path):
        return '{}/report{}'.format(self.local_server, path.split('report')[-1])

    def _del_dir(self):
        for time in return_y_d_m(ends_day_time=self.save):
            path = read_file('report', time)
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
        self.finish_dict['failure_list'] = self.failure
        self.finish_dict['unexpected_success_list'] = self.unexpected_success

    def _new_dict(self, value):
        return self._html(case_catalog=value[0], case_module=value[2],
                          case_level=value[1], case_name=value[3],
                          case_url=value[4], case_scene=value[5],
                          case_results=value[7], case_error_reason=value[8],
                          case_insert_parameter=value[9], status=value[6],
                          insert_time=value[14], case_wait_time=value[10],
                          case_author=value[12], case_img=value[11], case_remark=value[13])

    def _conversion_list(self, args):
        new_list = []
        for info in args:
            for case in info:
                for keys, value in enumerate(case):
                    self.new_dict[keys] = value
                new_list.append(dict(self.new_dict))
        return new_list

    def _html(self, case_catalog, case_module, case_level, case_name,
              case_url, case_scene, case_results, case_error_reason,
              case_insert_parameter, status, insert_time, case_wait_time,
              case_author, case_img, case_remark):

        html = GetTemplateHTML(case_catalog=case_catalog, case_module=case_module,
                               case_level=case_level, case_name=case_name,
                               case_url=case_url, case_scene=case_scene,
                               case_results=case_results, case_error_reason=case_error_reason,
                               case_insert_parameter=case_insert_parameter, status=status,
                               insert_time=insert_time, case_wait_time=case_wait_time,
                               case_author=case_author, case_img=case_img, case_remark=case_remark)
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
                        fraction=self.finish_dict['fraction'], url=self.local_server, local_url=self.wide_server,
                        execute_method=self.finish_dict['execute_method'],
                        execute_time=self.finish_dict['execute_time'],
                        project=self.finish_dict['project'],
                        failure_list=self.finish_dict['failure_list'],
                        unexpected_success_list=self.finish_dict['unexpected_success_list'],
                        failure_case=self.finish_dict['failure_case'],
                        unexpected_success_case=self.finish_dict['unexpected_case'])
        return html.replace('&lt;', '<').replace('&gt;', '>').replace('&#039;', '"').replace('&quot;', '"')


class ScreenShot(_Result, OperationElement):
    def __init__(self, url, img_path=None, switch=True):
        _Result.__init__(self)
        self.stream.writeln('HTML测试报告已完成，正在准备发送邮件中携带的附件...')
        driver = browser(switch)
        OperationElement.__init__(self, driver=driver)
        if img_path is None:
            self.path = read_file('img', 'html.png')
        else:
            self.path = img_path
        try:
            self.get(url)
            self.set_window_size(1800, 980)
            time.sleep(1)
            self.web_is_open(driver.title)
            self.screen_shot(self.path)
        except TimeoutException:
            self.stream.writeln('访问当前网站出错，请检查是否启动bottle服务...')
        except Exception as exc:
            self.stream.writeln('截图测试报告出错，出错原因: {}'.format(exc))
        finally:
            driver.quit()


class AmilSupport(MyReport):
    def __init__(self, case_data, switch=True, encoding='utf8', report_html_name='html_report'):
        MyReport.__init__(self)
        self.switch_browser = switch
        self.encoding = encoding
        self.report_html_name = report_html_name
        html_tpl_path = read_file('package/report/tpl', 'pie_link.tpl')
        title = MyConfig('project_name').excel_parameter
        scene = MyConfig('science').excel_parameter
        new_html = template(html_tpl_path, project_name=title,
                            scene=scene, error_count=case_data.get('errors'),
                            fail_count=case_data.get('failures'),
                            skip_count=case_data.get('skipped'),
                            success_count=case_data.get('success'),
                            guess_count=case_data.get('exceptionFail'),
                            accident_count=case_data.get('unexpectedSuccess'))
        self._save_as_report(new_html)

    def _save_as_report(self, case_name):
        """
        此方法主要用于，html存储
        :return: 返回对应的路径
        """
        path = read_file('report', '{}.html'.format(self.report_html_name))
        img_path = read_file('img', 'html.png')
        html = case_name.replace('&lt;', '<').replace('&gt;', '>').replace('&#039;', '"').replace('&quot;', '"')
        with open(path, 'wt', encoding=self.encoding) as f:
            f.writelines(html)
        url = self.local_server + '/report/{}.html'.format(self.report_html_name)
        ScreenShot(url, img_path, self.switch_browser)

