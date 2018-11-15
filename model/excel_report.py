import xlsxwriter
from config_path.path_file import get_excel_path, get_error_img_path


class WriteExcel:
    def __init__(self, *args, **kwargs):
        """初始化"""
        excel_ptah = get_excel_path()
        self.img_ptah = get_error_img_path()
        self.open_excel = xlsxwriter.Workbook(excel_ptah)
        self.style_title = self.open_excel.add_format()
        self.pc_style_title = self.open_excel.add_format()
        self.red = self.open_excel.add_format()
        self.blue = self.open_excel.add_format()
        self.test_content_style = self.open_excel.add_format()
        self.style_pc_content = self.open_excel.add_format()
        self.style_pc_title = self.open_excel.add_format()
        self.sheet_test = self.open_excel.add_worksheet(kwargs['sheet_test_info'])
        self.sheet_pc = self.open_excel.add_worksheet(kwargs['sheet_pc_config'])
        self.test_data_content = args

    def _test_title_style(self, style_font = '微软雅黑', font_size = 11, bold = False, bg_color = 'DeepSkyBlue'):
        """测试表单表头样式"""
        self.style_title.set_font_name(style_font)
        self.style_title.set_size(font_size)
        self.style_title.set_bold(bold)
        self.style_title.set_bg_color(bg_color)
        self.style_title.set_center_across()
        self.sheet_test.set_column(0, 0, 30)
        self.sheet_test.set_column(1, 1, 45)
        self.sheet_test.set_column(2, 2, 50)
        self.sheet_test.set_column(3, 4, 20)
        self.sheet_test.set_column(6, 6, 60)
        self.sheet_test.set_column(7, 7, 20)
        self.sheet_test.set_column(8, 8, 60)
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

    def write_test_title(self, *args):
        """写入测试表头/内容数据"""
        self._test_title_style()
        self._red_style()
        self._blue_style()
        self._test_content_style()
        for a, b in enumerate(args):
            self.sheet_test.write(0, a, b, self.style_title)
        for a, b in enumerate(self.test_data_content, 1):
            for c, d in enumerate(b):
                if '失败' == d:
                    self.sheet_test.write(a, c, d, self.red)
                    self.sheet_test.insert_image(a, c + 2, self.img_ptah, {'x_scale': 0.0757, 'y_scale': 0.076})
                elif '成功' == d:
                    self.sheet_test.write(a, c, d, self.blue)
                else:
                    self.sheet_test.set_row(a, 60)
                    self.sheet_test.write(a, c, d, self.test_content_style)
        self.open_excel.close()

    def _pc_title_style(self):
        """电脑配置表单表头样式"""
        self.sheet_pc.merge_range(0,0,)


if __name__ == '__main__':
    init = WriteExcel(
        ['登录首页', 'test/test/122', '场景', '336.225555577', '8888.555555555', '失败', 'SSSDDFDFD/**//*~!@#$%^&*()_+', '',
         '45646546SFDGD 鬼地方个回复的' * 90],
        ['用例名称', '测试地址', '场景', '最快响应时间(ms)', '最慢响应时间(ms)', '失败', '错误原因', '', '备注'],
        ['用例名称', '测试地址', '场景', '最快响应时间(ms)', '最慢响应时间(ms)', '成功', '错误原因', '', '备注'],
        sheet_test_info = '测试报告详情',
        sheet_pc_config = '计算机配置',
        )
    init.write_test_title('用例名称', '测试地址', '场景', '最快响应时间(ms)', '最慢响应时间(ms)', '状态', '错误原因', '截图', '备注', )
    #                 title = '电脑配置明细单',
    #                 cpu = 'cpu',
    #                 memory = '内存',
    #                 disk = '磁盘',
    #                 network = '网卡',
    #                 system = '操作系统',
    #                 real = '硬件消耗情况',
    #                 fix = '硬件配置情况',
    # )
