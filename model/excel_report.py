from config_path.path_file import get_excel_path,get_error_img_path
import xlwt,xlsxwriter


class WriteExcel:
    def __init__(self,*args,**kwargs):
        """初始化"""
        self.style_one = xlwt.XFStyle()
        self.style = xlwt.XFStyle()
        self.books = xlwt.Workbook()
        self.font = xlwt.Font()
        self.borders = xlwt.Borders()
        self.pattern = xlwt.Pattern()
        self.alignment = xlwt.Alignment()
        self.excel_path = get_excel_path()
        self.img_path = get_error_img_path()
        self._sheet = self.books.add_sheet(kwargs['sheet_report'])
        self._sheet_two = self.books.add_sheet(kwargs['sheet_pc'])
        self.data = args

    def borders_thin(self):
        """边框四周细实线"""
        self.borders.left = xlwt.Borders.THIN
        self.borders.right = xlwt.Borders.THIN
        self.borders.bottom = xlwt.Borders.THIN
        self.borders.top = xlwt.Borders.THIN
        self.style.borders = self.borders
        return self.style

    def pattern_background(self,color=14):
        """背景颜色"""
        # 1: 无；2：红色；3：大绿色；4/30/32/39：深蓝；5/34：浅黄；6/14：紫红；7：浅绿；8：深黑；9：白色；10：深红；11：深绿；12/35：大蓝；13：黄色
        # 23：灰色；25/27/41：浅绿；26/43：浅黄；28：深紫；29：橙色；31/42：浅绿绿；33：浅红；36：浅紫；37：土色；38：军绿；40：浅蓝；44：浅灰；45：浅土色
        self.pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        self.pattern.pattern_fore_colour = color
        self.style.pattern = self.pattern
        return self.style

    def font_underline(self):
        """字体下划线"""
        self.font.underline = True
        self.style.font = self.font
        return self.style

    def font_type(self,name='微软雅黑',height = 200,bold=False,colors=8):
        """字体"""
        self.font.name = name
        self.font.bold = bold
        self.font.height = height
        self.font.colour_index = colors
        self.style.font = self.font
        return self.style

    def alignment_left(self):
        """字体居中左对齐"""
        self.alignment.vert = xlwt.Alignment.VERT_CENTER
        self.alignment.horz = xlwt.Alignment.HORZ_LEFT
        self.style_one.alignment = self.alignment
        return self.style_one

    def merger_title_style(self,name='微软雅黑',height=200,color=40,bold=False,colors=8):
        """合并自定义样式"""
        self.style = self.font_type(name,height,bold,colors)
        self.style = self.pattern_background(color)
        self.style = self.alignment_center()
        return self.style

    def alignment_center(self):
        """字体居中对齐"""
        self.alignment.vert = xlwt.Alignment.VERT_CENTER
        self.alignment.horz = xlwt.Alignment.HORZ_CENTER
        self.style.alignment = self.alignment
        return self.style

    def excel_title(self,**kwargs):
        """用例定义Excel表头"""
        self._sheet.write(0,0,kwargs['case_name'],self.style)
        self._sheet.write(0,1,kwargs['test_url'],self.style)
        self._sheet.write(0,2,kwargs['response_fast'],self.style)
        self._sheet.write(0,3,kwargs['response_slow'],self.style)
        self._sheet.write(0,4,kwargs['status'],self.style)
        self._sheet.write(0,5,kwargs['error'],self.style)
        self._sheet.write(0,6,kwargs['screen_shot'],self.style)
        self._sheet.write(0,7,kwargs['remark'],self.style)
        self._sheet.col(0).width = 100*80
        self._sheet.col(1).width = 40*300
        self._sheet.col(2).width = 40*160
        self._sheet.col(3).width = 40*160
        self._sheet.col(4).width = 40*160
        self._sheet.col(5).width = 200*120
        self._sheet.col(6).width = 80*300
        self._sheet.col(7).width = 90*300

    def pc_config_info(self,**kwargs):
        """计算机定义Excel表头"""
        self.alignment_left()
        self.merger_title_style(bold = True)
        self._sheet_two.write_merge(1, 3, 0, 0, kwargs['cpu'],self.style_one)
        self._sheet_two.write_merge(4, 7, 0, 0, kwargs['disk'],self.style_one)
        self._sheet_two.write_merge(8, 11, 0, 0, kwargs['network'],self.style_one)
        self._sheet_two.write_merge(12, 15, 0, 0, kwargs['memory'],self.style_one)
        self._sheet_two.write_merge(16, 19, 0, 0, kwargs['system'],self.style_one)
        self._sheet_two.write_merge(0,0,0,6,kwargs['title'],self.style)
        self._sheet_two.col(0).width= 40 * 80
        self._sheet_two.col(1).width = 100 * 80
        self._sheet_two.col(2).width = 100 * 80
        self._sheet_two.col(3).width = 100 * 80
        self._sheet_two.col(4).width = 100 * 80
        self._sheet_two.col(5).width = 100 * 80
        self._sheet_two.col(6).width = 100 * 80

    def merge_excelStyle(self,**kwargs):
        """合并所有的Excel样式"""
        self.pc_config_info(**kwargs)
        self.excel_title(**kwargs)
        for a,b in enumerate(self.data,1):
            for c,d in enumerate(b):
                self._sheet.write(a,c,d)
        # self.books.save(self.excel_path)

    def pc_content(self,**kwargs):
        """写入计算机配置明细"""
        self._sheet_two.write(1,1,kwargs['sheet'])
        self.books.save(self.excel_path)

if __name__ == '__main__':
    init = WriteExcel(['首页','test/test/api/kl','254ms','11145ms','失败','账号不存在','',''],
                      [8,7,6,5,4,3,2,1],
                      sheet_report = '测试报告详情',
                      sheet_pc = '计算机配置',

    )
    init.merge_excelStyle(test_title = '测试的测试报告',
                     case_name = '用例名称',
                     test_url = '测试地址',
                     scene = '场景',
                     scene_one = '场景一',
                     scene_two = '场景二',
                     scene_three = '场景三',
                     response_fast = '最快响应时间(ms)',
                     response_slow = '最慢响应时间(ms)',
                     status = '状态',
                     error = '错误原因',
                     screen_shot = '截图',
                     remark = '备注',
                     title = '电脑配置明细单',
                     cpu = 'cpu',
                     memory = '内存',
                     disk = '磁盘',
                     network = '网卡',
                     system = '操作系统'
    )
    init.pc_content(sheet = '计算机配置',

    )
