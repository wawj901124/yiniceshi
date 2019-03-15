from datetime import datetime   #导入获取时间包

from django.db import models   #导入django的models
from django.contrib.auth.models import User #导入引用django默认新建user表的类User

from yinics.models import TestCase   #导入用例model


# Create your models here.
class CaseReport(models.Model):
    test_project = models.CharField(max_length=50, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=50,default="", verbose_name=u"测试模块")
    is_repeat = models.BooleanField(default=True,verbose_name="是否重复项目", help_text="是否重复项目")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"测试用例统计报告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.test_project

    #获取用例模块的所有项目名和模块名组合不重复的模块的名字及其id
    def get_testcase_all_projectandmodule_notrepeatname_nameandid(self):
        testcases = TestCase.objects.all()

        testcases_projectandmodule_name_list =[]
        testcases_projectandmodule_id_list = []
        for testcase in testcases:
            projectandmodule = "%s@#*pap%s"%(testcase.test_project,testcase.test_module)
            if  projectandmodule not in testcases_projectandmodule_name_list:
                testcases_projectandmodule_name_list.append(projectandmodule)
                testcases_projectandmodule_id_list.append(testcase.id)  # 将CaseReport中所有项目名和模块名组合不重复的id保存在一个列表里
        testcases_projectandmodule = []
        # print("testcases_projectandmodule_id_list:%s"% testcases_projectandmodule_id_list)
        # print("testcases_projectandmodule_id_list长度：%s" % len(testcases_projectandmodule_id_list))
        testcases_projectandmodule.append(testcases_projectandmodule_name_list)
        testcases_projectandmodule.append(testcases_projectandmodule_id_list)
        return testcases_projectandmodule

    #获取报告模块的所有项目名项目名和模块名组合不重复名字列表
    def get_casereport_projectandmodule_name_list(self):
        casereports_projectandmodule_name_list = []
        casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
        for casereport in casereports:
            casereports_projectandmodule_name_list.append("%s@#*pap%s"%(casereport.test_project,casereport.test_module))
        return casereports_projectandmodule_name_list

    #添加Testcase模块中所有项目及模块名
    def and_all_projectandmodule_name(self):
        testcases_projectandmodule = self.get_testcase_all_projectandmodule_notrepeatname_nameandid()
        casereports_projectandmodule_name_list = self.get_casereport_projectandmodule_name_list()
        testcases_projectandmodule_long = len(testcases_projectandmodule[0])
        if testcases_projectandmodule_long>0:
            for i in range(testcases_projectandmodule_long):
                if str(testcases_projectandmodule[0][i]) not in casereports_projectandmodule_name_list:
                    t = TestCase.objects.get(id=testcases_projectandmodule[1][i])
                    newcasereport = CaseReport()
                    newcasereport.test_project = t.test_project
                    newcasereport.test_module = t.test_module
                    newcasereport.save()
        return "添加所有项目及模块名"

    and_all_projectandmodule_name.short_description = u"添加所有项目及模块名"  # 定义xadmin中显示get_all_project_name函数返回值的键的名字

    def get_project_id_list(self):   #获取CaseReport项目名去重后的数据的id
        allcasereports = CaseReport.objects.all()
        project_name_list = []
        project_id_list = []
        for casereport in allcasereports:
            if casereport.test_project not in project_name_list:
                project_name_list.append(casereport.test_project)
                project_id_list.append(casereport.id)
        return project_id_list

    #设置casereport模块中项目名去重后的数据的is_repeat字段为不重复
    def set_is_repeat(self):
        project_id_list = self.get_project_id_list()
        if self.id in project_id_list:
            casereport = CaseReport.objects.get(id=self.id)
            casereport.is_repeat = '0'
            casereport.save()
            return '否'
        else:
            casereport = CaseReport.objects.get(id=self.id)
            casereport.is_repeat = '1'
            casereport.save()
            return  '是'

    set_is_repeat.short_description = u"是否重复项目"    #定义xadmin中显示is_repeat函数返回值的键的名字
    
    def goto(self,url,casenums):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'>{}</a>".format(url,casenums))


    def go_to_model_url(self,casenums,ex_result=None):   #定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        if ex_result==None:
            url = '{}/yinics/copytestcase/?_p_test_project__contains={}&_p_test_module__contains={}'.format(YMDK, self.test_project, self.test_module)
        else:
            url ='{}/yinics/copytestcase/?_p_test_project__contains={}&_p_test_module__contains={}&_p_ex_result__exact={}'.format(
            YMDK,self.test_project,self.test_module,ex_result)
        return self.goto(url=url,casenums=casenums)


    #获取某项目下某个模块的用例总数
    def get_case_model_total_nums(self):   #获取用例总数
        total_nums = TestCase.objects.filter(test_project=self.test_project).filter(test_module=self.test_module).count()
        return total_nums

    def goto_case_model_total_nums(self):#获取用例总数html链接
        total_nums = self.get_case_model_total_nums()
        return self.go_to_model_url(casenums=total_nums,ex_result=None)

    goto_case_model_total_nums.short_description = u"模块用例总数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # get_case_model_total_nums.short_description = u"用例总数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例通过数
    def get_case_model_pass_nums(self):   #获取用例通过数
        pass_nums = TestCase.objects.filter(test_project=self.test_project).filter(test_module=self.test_module).filter(ex_result='pass').count()
        return pass_nums

    def goto_case_model_pass_nums(self):#获取通过用例html链接
        pass_nums = self.get_case_model_pass_nums()
        return self.go_to_model_url(casenums=pass_nums,ex_result='pass')

    goto_case_model_pass_nums.short_description = u"模块用例通过数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例失败数
    def get_case_model_fail_nums(self):   #获取用例失败数
        fail_nums = TestCase.objects.filter(test_project=self.test_project).filter(test_module=self.test_module).filter(ex_result='fail').count()
        return fail_nums

    def goto_case_model_fail_nums(self):#获取失败用例html链接
        fail_nums = self.get_case_model_fail_nums()
        return self.go_to_model_url(casenums=fail_nums,ex_result='fail')

    goto_case_model_fail_nums.short_description = u"模块用例失败数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例锁定数
    def get_case_model_block_nums(self):   #获取用例锁定数
        block_nums = TestCase.objects.filter(test_project=self.test_project).filter(test_module=self.test_module).filter(ex_result='block').count()
        return block_nums

    def goto_case_model_block_nums(self):#获取锁定用例html链接
        block_nums = self.get_case_model_block_nums()
        return self.go_to_model_url(casenums=block_nums,ex_result='block')

    goto_case_model_block_nums.short_description = u"模块用例锁定数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例未执行数
    def get_case_model_na_nums(self):   #获取用例未执行数
        na_nums = TestCase.objects.filter(test_project=self.test_project).filter(test_module=self.test_module).filter(ex_result='na').count()
        return na_nums

    def goto_case_model_na_nums(self):#获取未执行用例html链接
        na_nums = self.get_case_model_na_nums()
        return self.go_to_model_url(casenums=na_nums,ex_result='na')

    goto_case_model_na_nums.short_description = u"模块用例未执行数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #计算通过率基函数
    def count_model_pass_lv_base(self,passnum,totalnum,nanum):
        jishu = totalnum-nanum
        if totalnum != 0:
            if jishu != 0:
                pass_lv = '通过率: {:.2f}%'.format(passnum/jishu*100)
                return pass_lv
            else:
                return '未执行用例'
        else:
            return '无用例'

    # 计算某项目下某个模块的用例通过率
    def count_model_pass_lv(self):
        passnum = self.get_case_model_pass_nums()
        totalnum = self.get_case_model_total_nums()
        nanum = self.get_case_model_na_nums()
        result = self.count_model_pass_lv_base(passnum,totalnum,nanum)
        return result

    count_model_pass_lv.short_description = u"模块用例通过率"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字


class CaseReportTwo(CaseReport):
    class Meta:
        verbose_name = u"项目统计"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表
                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.test_project

    def go_to_project_url_one(self,casenums):   #定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        url = '{}/casereport/casereport/?_p_test_project__contains={}'.format(YMDK,self.test_project)
        return self.goto(url=url,casenums=casenums)

    def go_to_project_url_two(self,casenums,ex_result=None):   #定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        if ex_result==None:
            url = '{}/yinics/copytestcase/?_p_test_project__contains={}'.format(YMDK, self.test_project, self.test_module)
        else:
            url ='{}/yinics/copytestcase/?_p_test_project__contains={}&_p_ex_result__exact={}'.format(
            YMDK,self.test_project,ex_result)
        return self.goto(url=url,casenums=casenums)


    def get_model_nums(self): #获取项目下的模块数
        model_nums = CaseReport.objects.filter(test_project=self.test_project).count()
        return model_nums

    def goto_model_nums(self):#获取
        model_nums = self.get_model_nums()
        return self.go_to_project_url_one(casenums=model_nums)

    goto_model_nums.short_description = u"项目下模块数"

    #获取某项目用例总数
    def get_case_project_total_nums(self):   #获取项目用例总数
        total_nums = TestCase.objects.filter(test_project=self.test_project).count()
        return total_nums

    def goto_case_project_total_nums(self):#获取用例总数html链接
        total_nums = self.get_case_project_total_nums()
        return self.go_to_project_url_two(casenums=total_nums,ex_result=None)

    goto_case_project_total_nums.short_description = u"项目用例总数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #获取某项目用例通过数
    def get_case_project_pass_nums(self):   #获取用例通过数
        pass_nums = TestCase.objects.filter(test_project=self.test_project).filter(ex_result='pass').count()
        return pass_nums

    def goto_case_project_pass_nums(self):#获取通过用例html链接
        pass_nums = self.get_case_project_pass_nums()
        return self.go_to_project_url_two(casenums=pass_nums,ex_result='pass')

    goto_case_project_pass_nums.short_description = u"项目用例通过数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #获取某项目用例失败数
    def get_case_project_fail_nums(self):   #获取用例失败数
        fail_nums = TestCase.objects.filter(test_project=self.test_project).filter(ex_result='fail').count()
        return fail_nums
    def goto_case_project_fail_nums(self):#获取失败用例html链接
        pass_nums = self.get_case_project_fail_nums()
        return self.go_to_project_url_two(casenums=pass_nums,ex_result='fail')

    goto_case_project_fail_nums.short_description = u"项目用例失败数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #获取某项目用例锁定数
    def get_case_project_block_nums(self):   #获取用例锁定数
        block_nums = TestCase.objects.filter(test_project=self.test_project).filter(ex_result='block').count()
        return block_nums
    def goto_case_project_block_nums(self):#获取通过用例html链接
        pass_nums = self.get_case_project_block_nums()
        return self.go_to_project_url_two(casenums=pass_nums,ex_result='block')

    goto_case_project_block_nums.short_description = u"项目用例锁定数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #获取某项目用例未执行数
    def get_case_project_na_nums(self):   #获取用例未执行数
        na_nums = TestCase.objects.filter(test_project=self.test_project).filter(ex_result='na').count()
        return na_nums
    def goto_case_project_na_nums(self):#获取通过用例html链接
        pass_nums = self.get_case_project_na_nums()
        return self.go_to_project_url_two(casenums=pass_nums,ex_result='na')

    goto_case_project_na_nums.short_description = u"项目用例未执行数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    #获取某项目用例通过数
    def count_project_pass_lv(self):
        passnum = self.get_case_project_pass_nums()
        totalnum = self.get_case_project_total_nums()
        nanum = self.get_case_project_na_nums()
        result = self.count_model_pass_lv_base(passnum, totalnum, nanum)
        return result

    count_project_pass_lv.short_description = u"项目用例通过率"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字