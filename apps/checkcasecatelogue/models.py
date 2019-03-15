from datetime import datetime  # 导入获取时间包

from django.db import models  # 导入django的models
from django.contrib.auth.models import User  # 导入引用django默认新建user表的类User

from yinics.models import TestCase  # 导入用例model


# Create your models here.
class CaseCatelogue(models.Model):
    test_project = models.CharField(max_length=100, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=100, default="", verbose_name=u"测试模块")
    test_page = models.CharField(max_length=100, default="", verbose_name=u"测试页面")
    is_repeat = models.BooleanField(default=True, verbose_name="是否重复项目", help_text="是否重复项目")
    is_repeat_model = models.BooleanField(default=True, verbose_name="是否重复模块", help_text="是否重复模块")
    add_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    class Meta:
        verbose_name = u"项目模块页面目录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.test_project

    # 获取用例模块的所有项目名和模块名组合不重复组合的名字及其id
    def get_testcase_all_projectandmodule_notrepeatname_nameandid(self):
        testcases = TestCase.objects.all()

        testcases_projectandmodule_name_list = []
        testcases_projectandmodule_id_list = []
        for testcase in testcases:
            projectandmoduleandpage = "%s@#*pap%s" % (testcase.test_project, testcase.test_module)
            if projectandmoduleandpage not in testcases_projectandmodule_name_list:
                testcases_projectandmodule_name_list.append(projectandmoduleandpage)
                testcases_projectandmodule_id_list.append(testcase.id)  # 将CaseReport中所有项目名和模块名和页面组合不重复的id保存在一个列表里
        testcases_projectandmodule = []
        # print("testcases_projectandmodule_id_list:%s"%testcases_projectandmodule_id_list)
        # print("testcases_projectandmodule_id_list长度:%s" % len(testcases_projectandmodule_id_list))
        testcases_projectandmodule.append(testcases_projectandmodule_name_list)
        testcases_projectandmodule.append(testcases_projectandmodule_id_list)
        return testcases_projectandmodule

    # 获取用例模块的所有项目名和模块名和页面名组合不重复组合的名字及其id
    def get_testcase_all_projectandmoduleandpage_notrepeatname_nameandid(self):
        testcases = TestCase.objects.all()

        testcases_projectandmoduleandpage_name_list = []
        testcases_projectandmoduleandpage_id_list = []
        for testcase in testcases:
            projectandmoduleandpage = "%s@#*pap%s@#*pap%s" % (testcase.test_project, testcase.test_module,testcase.test_page)
            if projectandmoduleandpage not in testcases_projectandmoduleandpage_name_list:
                testcases_projectandmoduleandpage_name_list.append(projectandmoduleandpage)
                testcases_projectandmoduleandpage_id_list.append(testcase.id)  # 将CaseReport中所有项目名和模块名和页面组合不重复的id保存在一个列表里
        testcases_projectandmoduleandpage = []
        # print("testcases_projectandmoduleandpage_id_list:%s"%testcases_projectandmoduleandpage_id_list)
        # print("testcases_projectandmoduleandpage_id_list长度:%s" % len(testcases_projectandmoduleandpage_id_list))
        # testcases_projectandmodule = self.get_testcase_all_projectandmodule_notrepeatname_nameandid()
        testcases_projectandmoduleandpage.append(testcases_projectandmoduleandpage_name_list)
        testcases_projectandmoduleandpage.append(testcases_projectandmoduleandpage_id_list)
        return testcases_projectandmoduleandpage

    # 获取用例目录模块的所有项目名和模块名和页面名组合不重复的名字列表
    def get_casecatelogue_projectandmoduleandpage_name_list(self):
        casecatelogue_projectandmoduleandpage_name_list = []
        casecatelogues = CaseCatelogue.objects.all()  # 获取CaseCatelogue所用内容
        for casecatelogue in casecatelogues:
            casecatelogue_projectandmoduleandpage_name_list.append(
                "%s@#*pap%s@#*pap%s" % (casecatelogue.test_project, casecatelogue.test_module,casecatelogue.test_page))
        return casecatelogue_projectandmoduleandpage_name_list

    # 添加Testcase模块中所有项目名和模块名和页面名字列表
    def and_all_projectandmoduleandpage_name(self):
        testcases_projectandmoduleandpage = self.get_testcase_all_projectandmoduleandpage_notrepeatname_nameandid()
        casecatelogue_projectandmoduleandpage_name_list = self.get_casecatelogue_projectandmoduleandpage_name_list()
        testcases_projectandmoduleandpage_long = len(testcases_projectandmoduleandpage[0])
        if testcases_projectandmoduleandpage_long > 0:
            for i in range(testcases_projectandmoduleandpage_long):
                if str(testcases_projectandmoduleandpage[0][i]) not in casecatelogue_projectandmoduleandpage_name_list:
                    t = TestCase.objects.get(id=testcases_projectandmoduleandpage[1][i])
                    newcasecatelogue = CaseCatelogue()
                    newcasecatelogue.test_project = t.test_project
                    newcasecatelogue.test_module = t.test_module
                    newcasecatelogue.test_page =t.test_page
                    newcasecatelogue.save()
        return "添加所有项目模块及页面名"
    and_all_projectandmoduleandpage_name.short_description = u"添加所有项目模块及页面名"  # 定义xadmin中显示and_all_projectandmoduleandpage_name函数返回值的键的名字

    def get_project_id_list(self):  # 获取CaseCatelogue项目名去重后的数据的id
        allcasecatelogues = CaseCatelogue.objects.all()
        project_name_list = []
        project_id_list = []
        for casecatelogue in allcasecatelogues:
            if casecatelogue.test_project not in project_name_list:
                project_name_list.append(casecatelogue.test_project)
                project_id_list.append(casecatelogue.id)

        return project_id_list

    # 设置casereport模块中项目名去重后的数据的is_repeat字段为不重复
    def set_is_repeat(self):
        project_id_list = self.get_project_id_list()

        if self.id in project_id_list:
            casecatelogue = CaseCatelogue.objects.get(id=self.id)
            casecatelogue.is_repeat= '0'
            casecatelogue.save()
            # print("save的id为：%s" % self.id)
            return '否'
        else:
            casecatelogue = CaseCatelogue.objects.get(id=self.id)
            casecatelogue.is_repeat = '1'
            casecatelogue.save()
            return '是'

    set_is_repeat.short_description = u"是否重复项目"  # 定义xadmin中显示is_repeat函数返回值的键的名字

    def get_projectandmodel_id_list(self):  # 获取CaseCatelogue项目模块名去重后的数据的id
        allcasecatelogues = CaseCatelogue.objects.all()
        projectandmodel_name_list = []
        projectandmodel_id_list = []
        for casecatelogue in allcasecatelogues:
            projectandmodule = "%s@#*pap%s" % (casecatelogue.test_project,casecatelogue.test_module)
            if projectandmodule not in projectandmodel_name_list:
                projectandmodel_name_list.append(projectandmodule)
                projectandmodel_id_list.append(casecatelogue.id)
        # print("projectandmodel_id_list:%s"% projectandmodel_id_list)
        # print("projectandmodel_id_list长度:%s" % len(projectandmodel_id_list))
        return projectandmodel_id_list

    # 设置casereport模块中项目模块名去重后的数据的is_repeat字段为不重复
    def set_is_repeat_model(self):
        projectandmodel_id_list = self.get_projectandmodel_id_list()
        # print("set_projectandmodel_id_list:%s"% projectandmodel_id_list)
        # print("set_projectandmodel_id_list长度:%s" % len(projectandmodel_id_list))
        if self.id in projectandmodel_id_list:
            casecatelogue = CaseCatelogue.objects.get(id=self.id)
            casecatelogue.is_repeat_model = '0'
            casecatelogue.save()
            return '否'
        else:
            casecatelogue = CaseCatelogue.objects.get(id=self.id)
            casecatelogue.is_repeat_model = '1'
            casecatelogue.save()
            return '是'

    set_is_repeat_model.short_description = u"是否重复模块"  # 定义xadmin中显示is_repeat函数返回值的键的名字

    def goto(self, url, casenums):  # 定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe  # 调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='{}'>{}</a>".format(url, casenums))

    def go_to_case_url(self, casenums,test_project=None,test_module=None,test_page=None):  # 定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        if test_page != None:
            url = '{}/yinics/copytwotestcase/?_p_test_project__contains={}&_p_test_module__contains={}&_p_test_page__contains={}'.format(YMDK,test_project,test_module,test_page)
        elif test_module != None:
            url = '{}/yinics/copytwotestcase/?_p_test_project__contains={}&_p_test_module__contains={}'.format(YMDK,test_project,test_module)
        else:
            url = '{}/yinics/copytwotestcase/?_p_test_project__contains={}'.format(YMDK,test_project)
        return self.goto(url=url, casenums=casenums)

    # 获取某项目下某个页面的用例总数
    def get_case_page_total_nums(self):  # 获取用例总数
        total_nums = TestCase.objects.filter(test_project=self.test_project).filter(
            test_module=self.test_module).filter(test_page=self.test_page).count()
        return total_nums

    def goto_case_page_total_nums(self):  # 获取用例总数html链接
        total_nums = self.get_case_page_total_nums()
        return self.go_to_case_url(casenums=total_nums,test_project=self.test_project,test_module=self.test_module,test_page=self.test_page)

    goto_case_page_total_nums.short_description = u"页面用例总数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字


class CaseCatelogueCopyTwo(CaseCatelogue):
    class Meta:
        verbose_name = u"项目模块目录"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表
                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.test_project

    def go_to_casecatelogue_url(self, casenums):  # 定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        url = '{}/checkcasecatelogue/casecatelogue/?_p_test_project__contains={}&_p_test_module__contains={}'.format(
            YMDK,self.test_project,self.test_module)
        return self.goto(url=url, casenums=casenums)

    # 获取某项目下某个模块的页面总数
    def get_page_total_nums(self):  # 获取用例总数
        total_nums = CaseCatelogue.objects.filter(test_project=self.test_project).filter(
            test_module=self.test_module).count()
        return total_nums

    def goto_page_total_nums(self):  # 获取用例总数html链接
        total_nums = self.get_page_total_nums()
        return self.go_to_casecatelogue_url(casenums=total_nums)

    goto_page_total_nums.short_description = u"模块下页面数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例总数
    def get_case_model_total_nums(self):  # 获取用例总数
        total_nums = TestCase.objects.filter(test_project=self.test_project).filter(
            test_module=self.test_module).count()
        return total_nums

    def goto_case_model_total_nums(self):  # 获取用例总数html链接
        total_nums = self.get_case_model_total_nums()
        return self.go_to_case_url(casenums=total_nums,test_project=self.test_project,test_module=self.test_module)

    goto_case_model_total_nums.short_description = u"模块用例总数"  # 定义xadmin中显示get_case_total_nums函数返回值的键的名字


class CaseCatelogueCopyThree(CaseCatelogueCopyTwo):
    class Meta:
        verbose_name = u"项目目录"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表
                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.test_project

    def go_to_casecateloguecopytwo_url(self, casenums):  # 定义点击后跳转到某一个地方（可以加html代码）
        from yiniceshi.settings import YMDK
        url = '{}/checkcasecatelogue/casecateloguecopytwo/?_p_test_project__contains={}'.format(
            YMDK,self.test_project)
        return self.goto(url=url, casenums=casenums)

    # 获取某项目下某个模块数
    def get_model_total_nums(self):  # 获取项目模块总数
        total_model_name_list = []
        caseCatelogues = CaseCatelogue.objects.filter(test_project=self.test_project)
        for caseCatelogue in caseCatelogues:
            if caseCatelogue.test_module not in total_model_name_list :
                total_model_name_list.append(caseCatelogue.test_module)
        total_nums = len(total_model_name_list)
        return total_nums

    def goto_model_total_nums(self):  # 获取用例总数html链接
        total_nums = self.get_model_total_nums()
        return self.go_to_casecateloguecopytwo_url(casenums=total_nums)

    goto_model_total_nums.short_description = u"项目下模块数"  # 定义xadmin中显示goto_case_project_total_nums函数返回值的键的名字

    # 获取某项目下某个模块的用例总数
    def get_case_project_total_nums(self):  # 获取用例总数
        total_nums = TestCase.objects.filter(test_project=self.test_project).count()
        return total_nums

    def goto_case_project_total_nums(self):  # 获取用例总数html链接
        total_nums = self.get_case_project_total_nums()
        return self.go_to_case_url(casenums=total_nums,test_project=self.test_project)

    goto_case_project_total_nums.short_description = u"项目用例总数"  # 定义xadmin中显示goto_case_project_total_nums函数返回值的键的名字

