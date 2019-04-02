from package.pie_link import HTML
from model.DriverParameter import browser
from config_path.path_file import read_file
from model.Yaml import MyYaml


class AmilSupport(object):
    def __init__(self, case_data, browser_switch=True, html_name='html_report', encoding='utf-8'):
        """该方法主要用于，邮件发送的一些支持类方法"""
        self.html_name = html_name
        self.encoding = encoding
        self.switch_browser = browser_switch
        self.title = MyYaml('project_name').excel_parameter
        self.science = MyYaml('science').excel_parameter
        self._browser_get_html(case_data)

    def _html_handle(self, case_data):
        """
        处理html中的数据
        :param case_data: 传过来的统计数据
        :return: 返回处理后的数据类型
        """
        return HTML % ('100%', '100%', '100%', self.title + 'UI统计简报', self.science,
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

