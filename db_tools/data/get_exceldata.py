# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from  db_tools.util.operation_excel import OperationExcel   #导入OperationExcel
from db_tools.data.exceldata_config import  *      #导入


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

    # 获取test_project
    def get_test_project(self,row):
        col = int(self.global_var.test_project)  #获取test_project所在的列数
        test_project = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return test_project

    #获取test_module
    def get_test_module(self,row):
        col = int(self.global_var.test_module)  #获取test_module所在的列数
        test_module = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return test_module

    # 获取test_page
    def get_test_page(self,row):
        col = int(self.global_var.test_page)  #获取test_page所在的列数
        test_page = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return test_page

    # 获取requirement_function
    def get_requirement_function(self,row):
        col = int(self.global_var.requirement_function)  #获取requirement_function所在的列数
        requirement_function = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return requirement_function

    # 获取case_priority
    def get_case_priority(self,row):
        col = int(self.global_var.case_priority)  #获取case_priority所在的列数
        case_priority = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_priority

    #获取case_process_type
    def get_case_process_type(self,row):
        col = int(self.global_var.case_process_type)  #获取case_process_type所在的列数
        case_process_type = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_process_type

    # 获取rele_case
    def get_rele_case(self,row):
        col = int(self.global_var.rele_case)  #获取rele_case所在的列数
        rele_case = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return rele_case

    # 获取case_title
    def get_case_title(self,row):
        col = int(self.global_var.case_title)  #获取case_title所在的列数
        case_title = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_title

    # 获取case_precondition
    def get_case_precondition(self,row):
        col = int(self.global_var.case_precondition)  #获取case_precondition所在的列数
        case_precondition = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_precondition

    #获取case_step
    def get_case_step(self,row):
        col = int(self.global_var.case_step)  #获取case_step所在的列数
        case_step = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_step

    # 获取case_expected_result
    def get_case_expected_result(self,row):
        col = int(self.global_var.case_expected_result)  #获取case_expected_result所在的列数
        case_expected_result = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return case_expected_result

    # 获取write_comments
    def get_write_comments(self,row):
        col = int(self.global_var.write_comments)  #获取write_comments所在的列数
        write_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return write_comments

    # 获取answer_comments
    def get_answer_comments(self,row):
        col = int(self.global_var.answer_comments)  #获取answer_comments所在的列数
        answer_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return answer_comments

    # 获取write_user
    def get_write_user(self,row):
        col = int(self.global_var.write_user)  #获取write_user所在的列数
        write_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return write_user

    #获取write_case_time
    def get_write_case_time(self,row):
        col = int(self.global_var.write_case_time)  #获取write_case_time所在的列数
        write_case_time = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return write_case_time

    # 获取ex_result
    def get_ex_result(self,row):
        col = int(self.global_var.ex_result)  #获取ex_result所在的列数
        ex_result = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return ex_result

    #获取write_case_time
    def get_test_comments(self,row):
        col = int(self.global_var.test_comments)  #获取test_comments所在的列数
        test_comments = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return test_comments

    # 获取test_user
    def get_test_user(self,row):
        col = int(self.global_var.test_user)  #获取test_user所在的列数
        test_user = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return test_user





if __name__ == '__main__':

    getdata = GetData()   #实例化
    print('---------------------------')
    rows_count = getdata.get_case_lines()
    for i in range(1, rows_count):  # 循环，但去掉第一个
        url = getdata.get_test_project(i)
        print(url)



