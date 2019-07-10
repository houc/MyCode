import xlsxwriter
import warnings
import os
import sys
import base64

from config_path.path_file import read_file
from model.PCParameter import merge_config_info, merge_config_msg, output_python_version
from model.Yaml import MyConfig


class WriteExcel:
    def __init__(self,*args, **kwargs):
        """初始化"""
        excel_ptah = read_file('report', 'case_info.xlsx')
        if not os.path.exists(excel_ptah):
            with open(excel_ptah, 'wt'):
                pass
        self.report_project = MyConfig('project_name').excel_parameter
        self.report_type = MyConfig('science').excel_parameter
        path = os.path.exists(read_file('img', 'logo.png'))
        if path:
            self.login_path = read_file('img', 'logo.png')
        else:
            self.login_path = False
        self.real_pc = merge_config_info()
        self.fix_pc = merge_config_msg()
        self.python_version = output_python_version()
        self.open_excel = xlsxwriter.Workbook(excel_ptah)
        self.style_title = self.open_excel.add_format()
        self.pc_style_title = self.open_excel.add_format()
        self.title_title = self.open_excel.add_format()
        self.title_title_content = self.open_excel.add_format()
        self.red = self.open_excel.add_format()
        self.blue = self.open_excel.add_format()
        self.skip = self.open_excel.add_format()
        self.yellow = self.open_excel.add_format()
        self.test_content_style = self.open_excel.add_format()
        self.style_pc_content = self.open_excel.add_format()
        self.style_pc_title = self.open_excel.add_format()
        self.sheet_title = self.open_excel.add_worksheet(kwargs['sheet_title'])
        self.sheet_test = self.open_excel.add_worksheet(kwargs['sheet_test_info'])
        self.sheet_pc = self.open_excel.add_worksheet(kwargs['sheet_pc_config'])
        self.test_data_content = args
        self.title_name = kwargs['sheet_title']

    def _test_title_style(self, style_font='微软雅黑', font_size=11, bold=False, bg_color='DeepSkyBlue'):
        """测试表单表头样式"""
        self.style_title.set_font_name(style_font)
        self.style_title.set_size(font_size)
        self.style_title.set_bold(bold)
        self.style_title.set_bg_color(bg_color)
        self.style_title.set_align('vcenter')
        self.style_title.set_center_across()

        # ===========这里是调试报告详情的行距宽度==============================

        self.sheet_test.set_column(0, 0, 25)
        self.sheet_test.set_column(1, 1, 10)
        self.sheet_test.set_column(2, 2, 20)
        self.sheet_test.set_column(3, 3, 30)
        self.sheet_test.set_column(4, 4, 40)
        self.sheet_test.set_column(5, 5, 50)
        self.sheet_test.set_column(6, 6, 8)
        self.sheet_test.set_column(7, 7, 30)
        self.sheet_test.set_column(8, 8, 40)
        self.sheet_test.set_column(9, 9, 18)
        self.sheet_test.set_column(10, 10, 34)
        self.sheet_test.set_column(11, 11, 10)
        self.sheet_test.set_column(12, 12, 20)
        return self.style_title

    def _red_style(self, color='red'):
        """测试内容默认为红色样式"""
        self.red.set_font_color(color)
        self.red.set_font_name('微软雅黑')
        self.red.set_size(11)
        self.red.set_border(7)
        self.red.set_align('vcenter')
        return self.red

    def _yellow_style(self, color='green'):
        """测试内容默认为黄色样式"""
        self.yellow.set_font_color(color)
        self.yellow.set_font_name('微软雅黑')
        self.yellow.set_size(11)
        self.yellow.set_border(7)
        self.yellow.set_align('vcenter')
        return self.yellow

    def _blue_style(self, color='blue'):
        """测试内容默认为蓝色样式"""
        self.blue.set_font_color(color)
        self.blue.set_size(11)
        self.blue.set_font_name('微软雅黑')
        self.blue.set_border(7)
        self.blue.set_align('vcenter')
        return self.blue

    def _skip_style(self):
        """跳过字体颜色"""
        self.skip.set_font_color('brown')
        self.skip.set_size(11)
        self.skip.set_font_name('微软雅黑')
        self.skip.set_border(7)
        self.skip.set_align('vcenter')
        return self.skip

    def _test_content_style(self, border=7):
        """内容样式,border:1:实线,2:加粗实线,3:间隙虚线,4:均匀虚线,
        5:更粗实线,6:双实线,7:点点虚线,8:加粗虚线,9:细虚线,10/12/13:加粗虚线"""
        self.test_content_style.set_font_name('微软雅黑')
        self.test_content_style.set_size(11)
        self.test_content_style.set_border(border)
        self.test_content_style.set_text_wrap()
        self.test_content_style.set_align('vcenter')
        return self.test_content_style

    def _write_test_title(self, *args):
        """写入测试表头/内容数据"""
        self._test_title_style()
        self._red_style()
        self._blue_style()
        self._skip_style()
        self._yellow_style()
        self._test_content_style()
        for a, b in enumerate(args):
            self.sheet_test.write(0, a, b, self.style_title)
        for e in self.test_data_content:
            for a, b in enumerate(e, 1):
                for c, d in enumerate(b):
                    if '失败' == d:
                        self.sheet_test.write(a, c, d, self.yellow)
                        path = _base64_conversion_img(img_name=b[3], base64=b[-3]).as_img
                        if not 'None' == path and path is not None:
                            self.sheet_test.insert_image(a, c + 4, path, {'x_scale': 0.127, 'y_scale': 0.169})
                    elif '成功' == d:
                        self.sheet_test.write(a, c, d, self.blue)
                    elif '错误' == d:
                        self.sheet_test.write(a, c, d, self.red)
                        path = _base64_conversion_img(img_name=b[3], base64=b[-3]).as_img
                        if not 'None' == path and path is not None:
                            self.sheet_test.insert_image(a, c + 4, path, {'x_scale': 0.127, 'y_scale': 0.169})
                    elif '跳过' == d:
                        self.sheet_test.write(a, c, d, self.skip)
                    elif 'None' == d:
                        self.sheet_test.write(a, c, '.........', self.test_content_style)
                    else:
                        self.sheet_test.set_row(a, 120)
                        if len(str(d)) >= 5000:
                            pass
                        else:
                            self.sheet_test.write(a, c, str(d), self.test_content_style)
        self.sheet_test.freeze_panes(1, 4)

    def _pc_title_style(self):
        """电脑配置表单表头样式"""
        self.sheet_pc.set_column(0, 1, 15)
        self.sheet_pc.set_column('C1:E1', 60)
        self.pc_style_title.set_bg_color('DeepSkyBlue')
        self.pc_style_title.set_align('vcenter')
        self.pc_style_title.set_center_across()
        self.pc_style_title.set_font_name('微软雅黑')
        self.pc_style_title.set_size(11)
        self.sheet_pc.freeze_panes(1, 0)
        return self.pc_style_title

    def _pc_content_style(self):
        """电脑配置内容样式"""
        self.style_pc_content.set_border(7)
        self.style_pc_content.set_size(11)
        self.style_pc_content.set_font_name('微软雅黑')
        self.style_pc_content.set_valign('vcenter')
        self.style_pc_content.set_text_wrap()
        return self.style_pc_content

    def _write_pc_content(self, **kwargs):
        """写入电脑配置表头/内容数据"""
        self._pc_title_style()
        self._pc_content_style()
        for i in range(20):
            self.sheet_pc.set_row(i + 1,20)
        self.sheet_pc.merge_range(0, 0, 0, 4, kwargs['title'], self.pc_style_title)
        self.sheet_pc.merge_range(1, 0, 4, 0, kwargs['CPU'], self.style_pc_content)
        self.sheet_pc.merge_range(5, 0, 8, 0, kwargs['memory'], self.style_pc_content)
        self.sheet_pc.merge_range(9, 0, 12, 0, kwargs['disk'], self.style_pc_content)
        self.sheet_pc.merge_range(13, 0, 16, 0, kwargs['network'], self.style_pc_content)
        self.sheet_pc.merge_range(17, 0, 20, 0, kwargs['system'], self.style_pc_content)
        self.sheet_pc.merge_range(1, 1, 2, 1, kwargs['consume'], self.style_pc_content)
        self.sheet_pc.merge_range(3, 1, 4, 1, kwargs['config'], self.style_pc_content)
        self.sheet_pc.merge_range(5, 1, 6, 1, kwargs['consume'], self.style_pc_content)
        self.sheet_pc.merge_range(7, 1, 8, 1, kwargs['config'], self.style_pc_content)
        self.sheet_pc.merge_range(9, 1, 10, 1, kwargs['consume'], self.style_pc_content)
        self.sheet_pc.merge_range(11, 1, 12, 1, kwargs['config'], self.style_pc_content)
        self.sheet_pc.merge_range(13, 1, 14, 1, kwargs['consume'], self.style_pc_content)
        self.sheet_pc.merge_range(15, 1, 16, 1, kwargs['config'], self.style_pc_content)
        self.sheet_pc.merge_range(17, 1, 18, 1, kwargs['consume'], self.style_pc_content)
        self.sheet_pc.merge_range(19, 1, 20, 1, kwargs['config'], self.style_pc_content)
        self.sheet_pc.merge_range(1, 2, 2, 4, str(self.real_pc[0]), self.style_pc_content)
        self.sheet_pc.merge_range(3, 2, 4, 4, str(self.fix_pc[0]), self.style_pc_content)
        self.sheet_pc.merge_range(5, 2, 6, 4, str(self.real_pc[3]), self.style_pc_content)
        self.sheet_pc.merge_range(7, 2, 8, 4, str(self.fix_pc[4]), self.style_pc_content)
        self.sheet_pc.merge_range(9, 2, 10, 4, str(self.real_pc[2]), self.style_pc_content)
        self.sheet_pc.merge_range(11, 2, 12, 4, str(self.fix_pc[3]), self.style_pc_content)
        self.sheet_pc.merge_range(13, 2, 14, 4, str(self.real_pc[4]), self.style_pc_content)
        self.sheet_pc.merge_range(15, 2, 16, 4, str(self.fix_pc[2]), self.style_pc_content)
        self.sheet_pc.merge_range(17, 2, 18, 4, str(self.real_pc[1]), self.style_pc_content)
        self.sheet_pc.merge_range(19, 2, 20, 4, str(self.fix_pc[1]), self.style_pc_content)

    def _title_title_style(self):
        """测试报告总览表单样式"""
        self.sheet_title.set_column('A1:F1', 18)
        self.sheet_title.set_column('D1:D1', 28)
        self.sheet_title.set_column('F1:F1', 28)
        self.title_title.set_border(7)
        self.title_title.set_font_name('微软雅黑')
        self.title_title.set_size(11)
        self.title_title.set_text_wrap()
        self.title_title.set_align('vcenter')
        self.title_title.set_align('center_across')
        self.title_title.set_bg_color('DeepSkyBlue')
        return self.title_title

    def _title_content_style(self):
        """测试报告表单内容"""
        self.title_title_content.set_border(7)
        self.title_title_content.set_text_wrap()
        self.title_title_content.set_valign('vcenter')
        self.title_title_content.set_font_name('微软雅黑')
        self.title_title_content.set_size(11)
        return self.title_title_content

    def _title_insert_report_img(self):
        """
        插入总体测试报告分析图表
        """
        title = self.title_name
        warnings.simplefilter('ignore')
        chart = self.open_excel.add_chart({
            'type':'column'
        })
        chart.add_series({
            'categories': '=(%s!$C$5,%s!$E$5,%s!$C$6,%s!$E$6,%s!$C$7)' % (title, title, title,
                                                                         title, title),
            'values': '=(%s!$D$5,%s!$F$5,%s!$D$6,%s!$F$6,%s!$D$7)' % (title, title, title,
                                                                     title, title),
            'points': [{'fill': {'color': 'blue'}},  # 总用例数
                      {'fill': {'color': 'green'}},  # 成功用例数
                      {'fill': {'color': 'yellow'}},  # 失败用例数
                      {'fill': {'color': 'red'}},  # 错误用例数
                      {'fill': {'color': 'orange'}}]
        })    # 跳过用例数
        chart.set_title({
            'name': f'{self.report_project}简报统计图'
        })
        chart.set_legend({
            'position': 'right'
        })
        chart.set_y_axis({
            'name': '个数'
        })
        chart.set_x_axis({
            'name': '状态'
        })
        self.sheet_title.insert_chart('A9', chart, {'x_scale': 1.93, 'y_scale': 1.60})

    def _title_write(self, parameter, **kwargs):
        """写入测试报告表头/内容数据"""
        self._title_title_style()
        self._title_content_style()
        self.sheet_title.merge_range(0, 0, 0, 5,
                                     str(kwargs['title_title']).format(self.report_project, self.report_type),
                                     self.title_title)
        self.sheet_title.merge_range(1, 0, 7, 1, ' ')
        if self.login_path:
            self.sheet_title.insert_image(3, 0, self.login_path, {'x_scale': 0.3, 'y_scale': 0.7})
        self.sheet_title.write(1, 2, kwargs['title_version'], self.title_title_content)
        self.sheet_title.write(1, 4, kwargs['title_action'], self.title_title_content)
        self.sheet_title.write(2, 2, kwargs['title_tool'], self.title_title_content)
        self.sheet_title.write(2, 4, kwargs['title_member'], self.title_title_content)
        self.sheet_title.write(3, 2, kwargs['title_start_time'], self.title_title_content)
        self.sheet_title.write(3, 4, kwargs['title_stop_time'], self.title_title_content)
        self.sheet_title.write(4, 2, kwargs['title_case'], self.title_title_content)
        self.sheet_title.write(4, 4, kwargs['title_success'], self.title_title_content)
        self.sheet_title.write(5, 2, kwargs['title_fail'], self.title_title_content)
        self.sheet_title.write(5, 4, kwargs['title_error'], self.title_title_content)
        self.sheet_title.write(6, 2, kwargs['skip'], self.title_title_content)
        self.sheet_title.write(6, 4, kwargs['total_time'], self.title_title_content)
        self.sheet_title.write(7, 2, kwargs['title_skip'], self.title_title_content)
        self.sheet_title.write(7, 4, kwargs['title_total_time'], self.title_title_content)

        # ======================================汇总表内容========================================

        if isinstance(parameter, dict):
            test_version = MyConfig("test_version").excel_parameter
            test_science = MyConfig("science").excel_parameter
            test_tool = 'Python'+ self.python_version
            self.sheet_title.write(1, 3, test_version, self.title_title_content)
            self.sheet_title.write(1, 5, test_science, self.title_title_content)
            self.sheet_title.write(2, 3, test_tool, self.title_title_content)
            self.sheet_title.write(2, 5, str(parameter.get("member")), self.title_title_content)
            self.sheet_title.write(3, 3, str(parameter.get("start_time")), self.title_title_content)
            self.sheet_title.write(3, 5, str(parameter.get("end_time")), self.title_title_content)
            self.sheet_title.write(4, 3, parameter.get("testsRun"), self.title_title_content)
            self.sheet_title.write(4, 5, parameter.get("success"), self.title_title_content)
            self.sheet_title.write(5, 3, parameter.get("failures"), self.title_title_content)
            self.sheet_title.write(5, 5, parameter.get("errors"), self.title_title_content)
            self.sheet_title.write(6, 3, parameter.get("skipped"), self.title_title_content)
            self.sheet_title.write(6, 5, parameter.get("total_time"), self.title_title_content)
            self.sheet_title.write(7, 3, str(parameter.get("short_time")), self.title_title_content)
            self.sheet_title.write(7, 5, str(parameter.get("long_time")), self.title_title_content)
            self._title_insert_report_img()
        else:
            raise TypeError('class_merge()函数方法应为字典')

    def _merge_def_title_data(self, parameter, *args, **kwargs):
        """函数进行封装"""
        self._title_write(parameter, **kwargs)
        self._write_pc_content(**kwargs)
        self._write_test_title(*args)
        self.open_excel.close()
        sys.stderr.write("excel测试报告已生成, 正在生成HTML形式报告...\n")


class ExcelTitle(WriteExcel):
    def __init__(self, *args):
        """
        初始化;
        args：用例，
        kwargs：整个表单的sheet
        """
        kwargs = {'sheet_test_info': '测试报告详情', 'sheet_pc_config': '计算机配置详情', 'sheet_title': '测试报告总览'}
        super(ExcelTitle, self).__init__(*args, **kwargs)

    def class_merge(self, parameter):
        """
        合并并传参->
        args：报告详情的表头，
        kwargs：PC配置中的表头/title_开头是报告里面的数据
        """
        args = '目录', '用例级别', '模块', '用例名称', '测试地址', '场景', '状态', '预期结果', \
               '异常原因（实际结果）', '用例执行时间', '截图', '负责人', '用例完成时间'
        kwargs = {'title': '测试机配置明细单', 'memory': '内存', 'disk': '磁盘', 'network': '网卡',
                  'system': '操作系统', 'consume': '硬件消耗情况', 'config': '硬件配置情况', 'CPU': 'CPU',
                  'title_title': '{}{}UI自动化测试报告', 'title_start_time': '开始时间', 'title_stop_time': '结束时间',
                  'title_total_time': '用例最长耗时', 'title_member':'编写用例人员', 'title_case': '总用例数',
                  'title_success': '成功数', 'title_fail': '失败数', 'title_error': '错误数', 'skip': '跳过数',
                  'title_skip': '用例最短耗时', 'total_time': '执行用例总耗时', 'title_action': '运行环境','title_tool': '测试工具',
                  'title_version': '测试版本',
                  }
        return self._merge_def_title_data(parameter, *args, **kwargs)


class _base64_conversion_img(object):
    def __init__(self, img_name, base64):
        self.base64 = base64
        self.path = read_file('img', '{}.png'.format(img_name))

    @property
    def as_img(self):
        if self.base64 and (not 'None' == self.base64):
            shot = base64.b64decode(self.base64.encode('ascii'))
            with open(self.path, 'wb') as f:
                f.write(shot)
            if os.path.exists(self.path):
                return self.path