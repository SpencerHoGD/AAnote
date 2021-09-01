import xlwt,os,xlrd
from xlutils.copy import copy

class Do_Excel:
    def __init__(self,filename,sheetname='Sheet1'):
        self.filename=filename
        self.sheetname=sheetname

    #读取excel，该部分可忽略 
    def excel_read(self,x, y):
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheetname)
        return table.cell(x, y).value

    #判断excel文件是否存在，不存在则创建，存在则直接打开编辑
    def excel_create(self):
        if not os.path.exists(self.filename):
            data = xlwt.Workbook()
            table = data.add_sheet(self.sheetname)
            table.write(0, 0, 'id')
            data.save(self.filename)
    
    #综合xlwt/xlrd/xlutils.copy,读写excel
    def write(self,i,j,value): 
        self.excel_create() 
        rb = xlrd.open_workbook(self.filename) 
        wb = copy(rb) #管道作用，通过get_sheet()获取的sheet有write()方法
        ws = wb.get_sheet(0) #1代表是写到第几个工作表里，从0开始算是第一个。
        ws.write(i, j, value) wb.save(self.filename) 

Do_Excel('test111.xlsx').write(1,1,'sdcds') 
Do_Excel('test111.xlsx').write(1,2,'ewewe')