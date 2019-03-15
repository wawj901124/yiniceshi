#独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","yiniceshi.settings")

import django
django.setup()

from yinics.models import TestCase

from db_tools.data.case_data import row_data

#对数据遍历入库
class ReadData:
    def readData(self):
        for lev1_cat in row_data:
            lev1_instance = TestCase()    #数据库的对象等于TestCase
            lev1_instance.test_project = lev1_cat["test_project"]
            lev1_instance.test_module = lev1_cat["test_module"]
            lev1_instance.test_page = lev1_cat["test_page"]
            lev1_instance.requirement_function = lev1_cat["requirement_function"]
            lev1_instance.case_priority = lev1_cat["case_priority"]
            lev1_instance.case_process_type = lev1_cat["case_process_type"]
            lev1_instance.case_title = lev1_cat["case_title"]
            lev1_instance.case_precondition = lev1_cat["case_precondition"]
            lev1_instance.case_step = lev1_cat["case_step"]
            lev1_instance.case_expected_result = lev1_cat["case_expected_result"]
            lev1_instance.write_comments = lev1_cat["write_comments"]
            # lev1_instance.wirte_user = lev1_cat["wirte_user"]
            lev1_instance.ex_result = lev1_cat["ex_result"]
            lev1_instance.test_comments = lev1_cat["test_comments"]
            lev1_instance.save()   #保存到数据库

if __name__ == "__main__":
    readdata = ReadData()  #实例化
    readdata.readData()