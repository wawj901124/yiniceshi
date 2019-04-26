#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","yiniceshi.settings")

import django
django.setup()

from yinics.models import TestCase

from db_tools.data.get_excelanswerdata import GetData


#对数据遍历入库
class ReadData:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name==None:
            self.filename = '../data/exceldata/answer.xls'
        else:
            self.filename = file_name

        if sheet_id ==None:
            self.sheetid = 0
        else:
            self.sheetid = sheet_id
        self.excelanswerdata = GetData(file_name=self.filename,sheet_id=self.sheetid)

    def readData(self):
        rows_count = self.excelanswerdata.get_case_lines()   #获取表的行数
        for i in range(1,rows_count):   #循环遍历表数据
            testcases = TestCase.objects.filter(id = self.excelanswerdata.get_id(i))
            for testcase in testcases:
                testcase.answer_comments = self.excelanswerdata.get_answer_comments(i)  #保存answer_comments
                testcase.save()   #保存到数据库


if __name__ == "__main__":
    readdata = ReadData(file_name=r"D:\Users\Administrator\PycharmProjects\yiniceshi\db_tools\data\exceldata\编写测试用例-20190425.xls")  #实例化
    readdata.readData()
