# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 18:27'
from django import forms    #导入django中的forms

from .models import TestCase  #导入TestCase模块


class TestCaseForm(forms.ModelForm):#定义处理前段“我要学习”表单类,继承ModelForm,ModelForm可以直接save,这个save调用的就是model的save，可以直接保存到数据库
    class Meta:
        model = TestCase   #指明转换的QSTestCase
        fields = ['test_project','test_module','test_page','requirement_function','case_priority',
                 'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
                  'write_comments','write_user','write_case_time']  #指明要转换的字段