# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 15:47'

import xlrd   #导入xlrd
from xlutils.copy import copy   #导入excel 复制函数

# data = xlrd.open_workbook('../dataconfig/merchantcontent.xls')   #打开excel文件
# tables = data.sheets()[0]   #获取excel表里的sheet表的索引值为0的表，即第一个表的内容
# print(tables.nrows)   #打印表的行数
# print(tables.cell_value(1,3))   #打印单元格里第二行第三列的内容


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = '../data/exceldata/测试用例模板.xls'

        if sheet_id:
            self.sheet_id = sheet_id
        else:
            self.sheet_id = 0


        self.data = self.get_data()   #获取sheet表


    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)  # 打开excel文件
        print("打开[%s]文件"% self.file_name)
        tables = data.sheets()[self.sheet_id]    #sheet_id从0开始
        print("遍历第%s个sheet表" % self.sheet_id)
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        print("获取到单元格的行数为%s"% tables.nrows)
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        print("获取【%s】行【%s】列的内容" % (row,col))
        return self.data.cell_value(row,col)

    #写入数据
    def write_value(self,row,col,value):
        """
        写入excel数据
        """
        read_data = xlrd.open_workbook(self.file_name)   #读到excel
        write_data = copy(read_data)   #复制excel
        sheet_data = write_data.get_sheet(0)   #得到excel中的sheet表中的第一个sheet表
        sheet_data.write(row,col,value)   #写入数据
        write_data.save(self.file_name)   #保存表


    #根据对应的caseid找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)   #先根据case_id拿到行号
        rows_data = self.get_row_values(row_num)   #再根据行号获取该行的内容
        return rows_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self,case_id):
        num = 0  #默认行号等于0
        clols_data = self.get_cols_data()   #获取某一列的内容
        for col_data in clols_data:   #循环
            if case_id in col_data:  #如果case_id等于某一列的数据，则返回该列的行数
                return num
            num = num + 1   #如果没有找到，行号自增1


    #根据行号找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):   #col_id=None,将col_id弄成一个可选参数
        if col_id !=None:
            cols = self.data.col_values(col_id)   #如果col_id 不为空，则返回col_id 的内容
        else:
            cols = self.data.col_values(0)   #否则默认返回第一行的内容
        return cols

if __name__ == '__main__':
    opers = OperationExcel()   #实例化
    print(opers.get_cell_value(1,1))   #打印表的行数



