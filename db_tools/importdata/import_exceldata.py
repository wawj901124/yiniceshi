#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","yiniceshi.settings")

import django
django.setup()

from yinics.models import TestCase

from db_tools.data.get_exceldata import GetData


#对数据遍历入库
class ReadData:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name==None:
            self.filename = '../data/exceldata/商户平台v1.5.1.xls'
        else:
            self.filename = file_name

        if sheet_id ==None:
            self.sheetid = 0
        else:
            self.sheetid = sheet_id
        self.exceldata = GetData(file_name=self.filename,sheet_id=self.sheetid)

    def readData(self):
        rows_count = self.exceldata.get_case_lines()   #获取表的行数
        for i in range(1,rows_count):   #循环遍历表数据
            testcase = TestCase()    #数据库的对象等于TestCase,实例化
            testcase.test_project = self.exceldata.get_test_project(i)   #填写项目
            testcase.test_module = self.exceldata.get_test_module(i)    #填写模块
            testcase.test_page = self.exceldata.get_test_page(i)   #填写测试页
            testcase.requirement_function = self.exceldata.get_requirement_function(i)   #填写功能点
            testcase.case_title = self.exceldata.get_case_title(i)   #填写用例名称
            testcase.case_precondition = self.exceldata.get_case_precondition(i)   #填写用例前提
            testcase.case_step = self.exceldata.get_case_step(i)   #填写用例步骤
            testcase.case_expected_result = self.exceldata.get_case_expected_result(i)   #填写用例预期结果
            testcase.write_comments = self.exceldata.get_write_comments(i)   #填写编写用例备注
            testcase.test_comments = self.exceldata.get_test_comments(i)   #填写测试备注
            testcase.save()  #保存到数据库


if __name__ == "__main__":
    readdata = ReadData(file_name=r"D:\Users\Administrator\PycharmProjects\yiniceshi\db_tools\data\exceldata\任务活动管理.xls")  #实例化
    readdata.readData()
