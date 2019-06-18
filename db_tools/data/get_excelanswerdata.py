# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from  db_tools.util.operation_excel import OperationExcel   #导入OperationExcel
from db_tools.data.excelanswerdata_config import  *      #导入


class GetData:
    def __init__(self,file_name=None,sheet_id=None):
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.opera_excel = OperationExcel(self.file_name,self.sheet_id)   #实例化
        self.global_var = GlobalVar()   #实例化


    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取id
    def get_id(self,row):
        col = int(self.global_var.id)  #获取id所在的列数
        id = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return id

    # 获取answer_comments
    def get_answer_comments(self,row):
        col = int(self.global_var.answer_comments)  #获取answer_comments所在的列数
        answer_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return answer_comments


if __name__ == '__main__':
    getdata = GetData(file_name=r'D:\Users\Administrator\PycharmProjects\yiniceshi\db_tools\data\exceldata\编写测试用例-20190429.xls')   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_test_project(i)
        print(url)



