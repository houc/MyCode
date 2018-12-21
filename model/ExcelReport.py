import xlsxwriter

from config_path.path_file import read_file
from model.PCParameter import merge_config_info,merge_config_msg
from model.Yaml import MyYaml


class WriteExcel:
    def __init__(self,*args, **kwargs):
        """初始化"""
        excel_ptah = read_file('report','ExcelReport.xlsx')
        self.report_project = MyYaml('project_name').excel_parameter
        self.report_type = MyYaml('science').excel_parameter
        self.login_path = read_file('img','logo.png')
        self.real_pc = merge_config_info()
        self.fix_pc = merge_config_msg()
        self.open_excel = xlsxwriter.Workbook(excel_ptah)
        self.style_title = self.open_excel.add_format()
        self.pc_style_title = self.open_excel.add_format()
        self.title_title = self.open_excel.add_format()
        self.title_title_content = self.open_excel.add_format()
        self.red = self.open_excel.add_format()
        self.blue = self.open_excel.add_format()
        self.test_content_style = self.open_excel.add_format()
        self.style_pc_content = self.open_excel.add_format()
        self.style_pc_title = self.open_excel.add_format()
        self.sheet_title = self.open_excel.add_worksheet(kwargs['sheet_title'])
        self.sheet_test = self.open_excel.add_worksheet(kwargs['sheet_test_info'])
        self.sheet_pc = self.open_excel.add_worksheet(kwargs['sheet_pc_config'])
        self.test_data_content = args

    def _test_title_style(self, style_font = '微软雅黑', font_size = 11, bold = False, bg_color = 'DeepSkyBlue'):
        """测试表单表头样式"""
        self.style_title.set_font_name(style_font)
        self.style_title.set_size(font_size)
        self.style_title.set_bold(bold)
        self.style_title.set_bg_color(bg_color)
        self.style_title.set_align('vcenter')
        self.style_title.set_center_across()
        self.sheet_test.set_column(0,0,5)
        self.sheet_test.set_column(1, 1, 10)
        self.sheet_test.set_column(2, 2, 50)
        self.sheet_test.set_column(3, 5, 50)
        self.sheet_test.set_column(6, 6, 8)
        self.sheet_test.set_column(7, 7, 50)
        self.sheet_test.set_column(8, 8, 60)
        self.sheet_test.set_column(9, 9, 100)
        self.sheet_test.set_column(10, 10, 60)
        return self.style_title

    def _red_style(self, color = 'red'):
        """测试内容默认为红色样式"""
        self.red.set_font_color(color)
        self.red.set_font_name('微软雅黑')
        self.red.set_size(11)
        self.red.set_border(7)
        self.red.set_align('vcenter')
        return self.red

    def _blue_style(self, color = 'blue'):
        """测试内容默认为蓝色样式"""
        self.blue.set_font_color(color)
        self.blue.set_size(11)
        self.blue.set_font_name('微软雅黑')
        self.blue.set_border(7)
        self.blue.set_align('vcenter')
        return self.blue

    def _test_content_style(self, border = 7):
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
        self._test_content_style()
        for a, b in enumerate(args):
            self.sheet_test.write(0, a, b, self.style_title)
        for e in self.test_data_content:
            for a, b in enumerate(e, 1):
                for c, d in enumerate(b):
                    if '失败' == d:
                        self.sheet_test.write(a, c, d, self.red)
                        self.sheet_test.insert_image(a, c + 2, b[-2], {'x_scale': 0.0757, 'y_scale': 0.099})
                    elif '成功' == d:
                        self.sheet_test.write(a, c, d, self.blue)
                    else:
                        self.sheet_test.set_row(a, 78)
                        self.sheet_test.write(a, c, d, self.test_content_style)
        self.sheet_test.freeze_panes(1,2)

    def _pc_title_style(self):
        """电脑配置表单表头样式"""
        self.sheet_pc.set_column(0,1,15)
        self.sheet_pc.set_column('C1:E1',60)
        self.pc_style_title.set_bg_color('DeepSkyBlue')
        self.pc_style_title.set_align('vcenter')
        self.pc_style_title.set_center_across()
        self.pc_style_title.set_font_name('微软雅黑')
        self.pc_style_title.set_size(11)
        self.sheet_pc.freeze_panes(1,0)
        return self.pc_style_title

    def _pc_content_style(self):
        """电脑配置内容样式"""
        self.style_pc_content.set_border(7)
        self.style_pc_content.set_size(11)
        self.style_pc_content.set_font_name('微软雅黑')
        self.style_pc_content.set_valign('vcenter')
        self.style_pc_content.set_text_wrap()
        return self.style_pc_content

    def _write_pc_content(self,**kwargs):
        """写入电脑配置表头/内容数据"""
        self._pc_title_style()
        self._pc_content_style()
        for i in range(20):
            self.sheet_pc.set_row(i + 1,20)
        self.sheet_pc.merge_range(0,0,0,4,kwargs['title'],self.pc_style_title)
        self.sheet_pc.merge_range(1,0,4,0,kwargs['CPU'],self.style_pc_content)
        self.sheet_pc.merge_range(5,0,8,0,kwargs['memory'],self.style_pc_content)
        self.sheet_pc.merge_range(9,0,12,0,kwargs['disk'],self.style_pc_content)
        self.sheet_pc.merge_range(13,0,16,0,kwargs['network'],self.style_pc_content)
        self.sheet_pc.merge_range(17,0,20,0,kwargs['system'],self.style_pc_content)
        self.sheet_pc.merge_range(1,1,2,1,kwargs['consume'],self.style_pc_content)
        self.sheet_pc.merge_range(3,1,4,1,kwargs['config'],self.style_pc_content)
        self.sheet_pc.merge_range(5,1,6,1,kwargs['consume'],self.style_pc_content)
        self.sheet_pc.merge_range(7,1,8,1,kwargs['config'],self.style_pc_content)
        self.sheet_pc.merge_range(9,1,10,1,kwargs['consume'],self.style_pc_content)
        self.sheet_pc.merge_range(11,1,12,1,kwargs['config'],self.style_pc_content)
        self.sheet_pc.merge_range(13,1,14,1,kwargs['consume'],self.style_pc_content)
        self.sheet_pc.merge_range(15,1,16,1,kwargs['config'],self.style_pc_content)
        self.sheet_pc.merge_range(17,1,18,1,kwargs['consume'],self.style_pc_content)
        self.sheet_pc.merge_range(19,1,20,1,kwargs['config'],self.style_pc_content)
        self.sheet_pc.merge_range(1,2,2,4,str(self.real_pc[0]),self.style_pc_content)
        self.sheet_pc.merge_range(3,2,4,4,str(self.fix_pc[0]),self.style_pc_content)
        self.sheet_pc.merge_range(5,2,6,4,str(self.real_pc[3]),self.style_pc_content)
        self.sheet_pc.merge_range(7,2,8,4,str(self.fix_pc[4]),self.style_pc_content)
        self.sheet_pc.merge_range(9,2,10,4,str(self.real_pc[2]),self.style_pc_content)
        self.sheet_pc.merge_range(11,2,12,4,str(self.fix_pc[3]),self.style_pc_content)
        self.sheet_pc.merge_range(13,2,14,4,str(self.real_pc[4]),self.style_pc_content)
        self.sheet_pc.merge_range(15,2,16,4,str(self.fix_pc[2]),self.style_pc_content)
        self.sheet_pc.merge_range(17,2,18,4,str(self.real_pc[1]),self.style_pc_content)
        self.sheet_pc.merge_range(19,2,20,4,str(self.fix_pc[1]),self.style_pc_content)

    def _title_title_style(self):
        """测试报告总览表单样式"""
        self.sheet_title.set_column('A1:F1',14)
        self.title_title.set_font_name('微软雅黑')
        self.title_title.set_size(11)
        self.title_title.set_text_wrap()
        self.title_title.set_align('vcenter')
        self.title_title.set_align('center_across')
        self.title_title.set_bg_color('DeepSkyBlue')
        return self.title_title

    def _title_content_style(self):
        """测试报告表单内容"""
        self.title_title_content.set_text_wrap()
        self.title_title_content.set_valign('vcenter')
        self.title_title_content.set_font_name('微软雅黑')
        self.title_title_content.set_size(11)
        return self.title_title_content

    def _title_insert_report_img(self):
        """插入总体测试报告分析图表"""
        img = self.open_excel.add_chart({'type':'column'})
        img.add_series(
            {
                'name': '分析',
                'categories': '={}!$A$1:$D$1'.format(self.sheet_title),
                'values': '={}!$A$2:$D$2'.format(self.sheet_title),
                'fill': {'color': '#FF9900'},
            }
        )
        img.set_x_axis(
            {
                'name': '错误',
                'name_font': {'size': 10},
                'min':2,
                'max':5,
            }
        )
        img.set_y_axis(
            {
                'name': '的',
                'name_font': {'size': 14, 'bold': True},
                'num_font': {'italic': True},
                'min': 20,
                'max': 50,
            }
        )
        self.sheet_title.insert_chart('A10',img)
        return self.sheet_title

    def _title_write(self,parameter,**kwargs):
        """写入测试报告表头/内容数据"""
        self._title_title_style()
        self._title_content_style()
        self.sheet_title.merge_range(0,0,0,5,str(kwargs['title_title']).format(self.report_project,self.report_type),self.title_title)
        self.sheet_title.merge_range(1,0,6,1,' ')
        self.sheet_title.set_zoom(120)
        self.sheet_title.insert_image(1,0,self.login_path,{'x_scale': 0.822,'y_scale': 0.863})
        self.sheet_title.write(1,2,kwargs['title_version'],self.title_title_content)
        self.sheet_title.write(1,4,kwargs['title_action'],self.title_title_content)
        self.sheet_title.write(2,2,kwargs['title_tool'],self.title_title_content)
        self.sheet_title.write(2,4,kwargs['title_member'],self.title_title_content)
        self.sheet_title.write(3,2,kwargs['title_start_time'],self.title_title_content)
        self.sheet_title.write(3,4,kwargs['title_stop_time'],self.title_title_content)
        self.sheet_title.write(4,2,kwargs['title_case'],self.title_title_content)
        self.sheet_title.write(4,4,kwargs['title_success'],self.title_title_content)
        self.sheet_title.write(5,2,kwargs['title_fail'],self.title_title_content)
        self.sheet_title.write(5,4,kwargs['title_error'],self.title_title_content)
        self.sheet_title.write(6,2,kwargs['title_skip'],self.title_title_content)
        self.sheet_title.write(6,4,kwargs['title_total_time'],self.title_title_content)
        if isinstance(parameter,list):
            print()
        else:
            raise TypeError('class_merge()函数方法应为["A","B","C","D"]')

    def _merge_def_title_data(self,parameter,*args,**kwargs):
        """函数进行封装"""
        self._title_write(parameter,**kwargs)
        self._write_pc_content(**kwargs)
        self._write_test_title(*args)
        self.open_excel.close()


class ExcelTitle(WriteExcel):
    def __init__(self,*args):
        """初始化，args：用例，kwargs：整个表单的sheet"""
        kwargs = {'sheet_test_info':'测试报告详情','sheet_pc_config':'计算机配置详情','sheet_title':'测试报告总览'}
        super(ExcelTitle, self).__init__(*args, **kwargs)

    def class_merge(self,parameter):
        """合并并传参；args：报告详情的表头，kwargs：PC配置中的表头/title_开头是报告里面的数据"""
        args = '#','用例级别','用例名称', '测试地址', '场景', '用例响应时间', '状态', '错误原因', '截图', '备注',
        kwargs = {'title':'测试机配置明细单','memory':'内存','disk':'磁盘','network':'网卡','system':'操作系统','consume':'硬件消耗情况','config':'硬件配置情况','CPU':'CPU',
                  'title_title':'{}项目{}自动化测试报告','title_start_time':'开始时间','title_stop_time':'结束时间','title_total_time':'总用时','title_member':'参与人员',
                  'title_case':'总用例数','title_success':'成功数','title_fail':'失败数','title_error':'错误数','title_skip':'跳过数','':'',
                  'title_action':'测试环境','title_tool':'测试工具','title_version':'测试版本'
                  }
        return self._merge_def_title_data(parameter,*args,**kwargs)


if __name__ == '__main__':
    ExcelTitle([['1','P0','登录', 'test/122', '符合规范的', '1.256s', '成功', '辅导费333', 'd:/','苟富贵'],
                ['1', 'P0', '登录', 'test/122', '符合规范的', '1.256s', '成功', '辅导费333', 'c:/', '苟富贵'],]

    ).class_merge(['w','u'])
