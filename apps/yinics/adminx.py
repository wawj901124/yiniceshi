# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 10:19'

from django.contrib.auth.models import User #导入引用django默认新建user表的类User

import xadmin
from xadmin import views   #导入xadmin中的views,用于和 BaseSettings类绑定


from .models import TestCase,CopyTestCase,CopyTwoTestCase #导入模型
from casereport.models import CaseReport   #导入CaseReport
from checkcasecatelogue.models import CaseCatelogue   #导入CaseCatelogue



class TestCaseAdmin(object):
    ziduan = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type','rele_case', 'case_title','case_precondition', 'case_step',
              'case_expected_result','write_comments','answer_comments','write_case_time']


    list_display =['id','test_project','test_module','test_page','requirement_function','case_priority',
                   'case_process_type', 'rele_case', 'case_title','case_precondition', 'case_step',
                   'case_expected_result','write_comments','answer_comments','write_user','write_case_time',
                   'go_to','go_more'] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'write_comments']
    list_filter = ['test_project','test_module','test_page','case_priority','case_process_type','case_title','write_comments',]   #定义筛选的字段
    model_icon = 'fa fa-tasks'  # 定义图标显示
    ordering = ['-write_case_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ['write_case_time','write_user','test_user']  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project','case_title',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project','case_title',]   #显示数据详情

    #设置是否加入导入插件
    import_excel = True   #True表示显示使用插件，False表示不显示使用插件，该import_excel变量会覆盖插件中的变量

    #设置空值显示
    # empty_value_display = "无相关内容"  #没用，不生效


    def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
        #在保存用例的时候统计新加用例项目名字是否新加，模块名字是否新加，以及新加数，以及在用户报告模块中自动新加内容
        obj = self.new_obj   #取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:    #非超级用户会自动保存编写人
            user = User.objects.get(username=self.request.user)
            obj.write_user_id = user.id  #保存当前的write_user为用户登录的user
            obj.save()   #保存当前用例

        casereports_projectandmodule_name_list = []
        casereports_project_name_list = []
        casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
        for casereport in casereports:
            casereports_project_name_list.append(casereport.test_project)
            casereports_projectandmodule_name_list.append("%s@#*pap%s"%(casereport.test_project,casereport.test_module))

        newaddtestcase = "%s@#*pap%s"%(obj.test_project,obj.test_module)

        if newaddtestcase not in casereports_projectandmodule_name_list:
            newcasereport = CaseReport()
            newcasereport.test_project = obj.test_project
            newcasereport.test_module =obj.test_module
            if obj.test_project not in casereports_project_name_list:
                newcasereport.is_repeat = False
            newcasereport.save()

        casecatelogues_projectandmoduleandpage_name_list = []
        casecatelogues_projectandmodule_name_list = []
        casecatelogues_project_name_list = []
        casecatelogues = CaseCatelogue.objects.all() # 获取CaseCatelogue所用内容
        for casecatelogue in casecatelogues:
            casecatelogues_project_name_list.append(casecatelogue.test_project)
            casecatelogues_projectandmodule_name_list.append("%s@#*pap%s"% (casecatelogue.test_project,casecatelogue.test_module))
            casecatelogues_projectandmoduleandpage_name_list.append("%s@#*pap%s@#*pap%s"% (casecatelogue.test_project,casecatelogue.test_module,casecatelogue.test_page))
        newaddtestcase_addpage = "%s@#*pap%s@#*pap%s"% (obj.test_project,obj.test_module,obj.test_page)
        if newaddtestcase_addpage not in casecatelogues_projectandmoduleandpage_name_list:
            newcasecatelogue = CaseCatelogue()
            newcasecatelogue.test_project = obj.test_project
            newcasecatelogue.test_module = obj.test_module
            newcasecatelogue.test_page = obj.test_page
            if newaddtestcase not in casecatelogues_projectandmodule_name_list:
                newcasecatelogue.is_repeat_model = False
            if obj.test_project not in casecatelogues_project_name_list:
                newcasecatelogue.is_repeat = False
            newcasecatelogue.save()

    def post(self,request, *args,**kwargs):   #重载post函数，用于判断导入的逻辑
        if 'excel' in request.FILES:  #如果excel在request.FILES中
            excel_file = request.FILES.get('excel', '')


            import xlrd   #导入xlrd
            #常用的Excel文件有.xls和.xls两种，.xls文件读取时需要设置formatting_info = True
            # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件

            exceldata = xlrd.open_workbook(filename=None, file_contents=excel_file.read(), formatting_info=True)  # xls文件

            from .analyzexls import Analyzexls
            analyzexls = Analyzexls()
            #将获取的数据循环导入数据库中
            all_list_1 = analyzexls.get_sheets_mg(exceldata, 0)
            i = 0
            if len(all_list_1[0]) == 21:
                while i < len(all_list_1):
                    testcase = TestCase()  # 数据库的对象等于TestCase,实例化
                    testcase.test_project = all_list_1[i][1]  # 填写项目all_list_1[i][j]
                    testcase.test_module = all_list_1[i][2]  # 填写模块
                    testcase.test_page = all_list_1[i][3]  # 填写测试页
                    testcase.requirement_function = all_list_1[i][4]  # 填写功能点
                    testcase.case_title = all_list_1[i][8] # 填写用例名称
                    testcase.case_precondition = all_list_1[i][9]  # 填写用例前提
                    testcase.case_step = all_list_1[i][10]  # 填写用例步骤
                    testcase.case_expected_result = all_list_1[i][11]  # 填写用例预期结果
                    testcase.write_comments = all_list_1[i][12]  # 填写编写用例备注
                    testcase.answer_comments = all_list_1[i][13]  # 填写问题答复
                    if all_list_1[i][14] != None:  # 如果编写人列有数据则填写编写人
                        users = User.objects.all()
                        for user in users:
                            if user.username == all_list_1[i][14]:
                                testcase.write_user_id = user.id   # 填写编写人
                    testcase.test_comments = all_list_1[i][19]  # 填写测试备注
                    testcase.save()  # 保存到数据库

                    #处理CaseReport相关内容
                    casereports_projectandmodule_name_list = []
                    casereports_project_name_list = []
                    casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
                    print("casereports.count():%s"% casereports.count())
                    for casereport in casereports:
                        casereports_project_name_list.append(casereport.test_project)
                        casereports_projectandmodule_name_list.append(
                            "%s@#*pap%s" % (casereport.test_project, casereport.test_module))

                    newaddtestcase = "%s@#*pap%s" % (all_list_1[i][1], all_list_1[i][2])
                    print("casereports_projectandmodule_name_list：%s" % casereports_projectandmodule_name_list )
                    print("casereports_project_name_list:%s" % casereports_project_name_list)

                    if newaddtestcase not in casereports_projectandmodule_name_list:
                        newcasereport = CaseReport()
                        newcasereport.test_project = all_list_1[i][1]
                        newcasereport.test_module = all_list_1[i][2]
                        if all_list_1[i][1] not in casereports_project_name_list:
                            newcasereport.is_repeat = False
                        newcasereport.save()

                    # 处理CaseCatelogue相关内容
                    casecatelogues_projectandmoduleandpage_name_list = []
                    casecatelogues_projectandmodule_name_list = []
                    casecatelogues_project_name_list = []
                    casecatelogues = CaseCatelogue.objects.all()  # 获取CaseCatelogue所用内容
                    print("casecatelogues.count():%s" % casecatelogues.count())
                    for casecatelogue in casecatelogues:
                        casecatelogues_project_name_list.append(casecatelogue.test_project)
                        casecatelogues_projectandmodule_name_list.append("%s@#*pap%s" % (casecatelogue.test_project, casecatelogue.test_module))
                        casecatelogues_projectandmoduleandpage_name_list.append("%s@#*pap%s@#*pap%s" % (casecatelogue.test_project, casecatelogue.test_module, casecatelogue.test_page))
                    newaddtestcase_addpage = "%s@#*pap%s@#*pap%s" % (all_list_1[i][1],all_list_1[i][2],all_list_1[i][3])
                    print("casecatelogues_projectandmoduleandpage_name_list:%s" % casecatelogues_projectandmoduleandpage_name_list)
                    print("casecatelogues_projectandmodule_name_list:%s" %  casecatelogues_projectandmodule_name_list)
                    print("casecatelogues_project_name_list:%s" % casecatelogues_project_name_list)
                    print("newaddtestcase_addpage:%s" % newaddtestcase_addpage)
                    print("newaddtestcase:%s" % newaddtestcase)
                    if newaddtestcase_addpage not in casecatelogues_projectandmoduleandpage_name_list:
                        newcasecatelogue = CaseCatelogue()
                        newcasecatelogue.test_project = all_list_1[i][1]
                        newcasecatelogue.test_module = all_list_1[i][2]
                        newcasecatelogue.test_page = all_list_1[i][3]
                        if newaddtestcase not in casecatelogues_projectandmodule_name_list:
                            newcasecatelogue.is_repeat_model = False
                        if all_list_1[i][1] not in casecatelogues_project_name_list:
                            newcasecatelogue.is_repeat = False
                        newcasecatelogue.save()

                    i = i+1
            pass
        return super(TestCaseAdmin,self).post(request,args,kwargs)   #必须调用TestCaseAdmin父类，再调用post方法，否则会报错
                                                                      #一定不要忘记，否则整个TestCaseAdmin保存都会出错




    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(TestCaseAdmin, self).queryset()   #调用父类
        if self.request.user.is_superuser:   #超级用户可查看所有数据
            return qs
        else:
            qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
            return qs   #返回qs

xadmin.site.register(TestCase, TestCaseAdmin) #在xadmin中注册QSTestCase


class CopyTestCaseAdmin(object):
    ziduan = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'write_comments','write_case_time','ex_result','test_comments']

    list_display =[ 'case_title','case_precondition', 'case_step', 'case_expected_result','ex_result',
                    'test_comments',] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'test_comments','write_comments',]
    list_filter = ['test_project','test_module','test_page','case_priority','case_process_type','write_comments','ex_result','test_comments']   #定义筛选的字段
    model_icon = 'fa fa-play'  # 定义图标显示
    ordering = ['write_case_time']  # 添加默认排序规则显示排序，根据添加时间正序排序
    readonly_fields = ['write_user','test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'write_comments','write_case_time','rele_case','test_user']  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    list_editable = ['ex_result','test_comments',]  # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project','case_title',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project','case_title',]   #显示数据详情

    # def queryset(self):
    #     qs = super(CopyTestCaseAdmin, self).queryset()
    #     if self.request.user.is_superuser:  # 超级用户可查看所有数据
    #         return qs
    #     else:
    #         return qs.filter(write_user=self.request.user)  # user是Model的write_user字段

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     """对外键进行设置"""
    #     if db_field.name == 'write_user':
    #         kwargs['initial'] = request.user.id
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(CopyTestCaseAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs
    #     )

    # def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(CopyTestCaseAdmin, self).queryset()   #调用父类
    #     if self.request.user.is_superuser:   #超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
    #         return qs   #返回qs
    # def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
    #     #在保存用例的时候统计新加用例项目名字是否新加，模块名字是否新加，以及新加数，以及在用户报告模块中自动新加内容
    #     obj = self.new_obj   #取得当前用例的实例
    #     obj.save()   #保存当前用例
    #
    #     casereports = CaseReport.objects.all()   #获取CaseReport所用内容
    #     casereport_project_name_list =[]
    #     casereport_module_name_list = []
    #     for casereport in casereports:
    #         casereport_project_name_list.append(casereport.test_project)  #将CaseReport中所有项目名保存在一个列表里
    #         casereport_module_name_list.append(casereport.test_module)   #将CaseReport中所有模块名保存在一个列表里
    #
    #     if obj.test_project not in casereport_project_name_list:  #如果新加用例的项目名不在CaseReport项目中，则新加一条数据
    #         newcasereport = CaseReport()
    #         newcasereport.test_project = obj.test_project
    #         newcasereport.test_module =obj.test_module
    #         newcasereport.save()
    #     elif obj.test_module not in casereport_module_name_list:
    #         newcasereport = CaseReport()
    #         newcasereport.test_project = obj.test_project
    #         newcasereport.test_module =obj.test_module
    #         newcasereport.save()
    def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
        #在保存用例的时候统计新加用例项目名字是否新加，模块名字是否新加，以及新加数，以及在用户报告模块中自动新加内容
        obj = self.new_obj   #取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:    #非超级用户会自动保存编写人
            if obj.test_user_id == None:
                user = User.objects.get(username=self.request.user)
                obj.test_user_id = user.id  #保存当前的test_user为用户登录的user
            obj.save()   #保存当前用例


xadmin.site.register(CopyTestCase, CopyTestCaseAdmin) #在xadmin中注册CopyWriteTestCase


class CopyTwoTestCaseAdmin(object):
    ziduan = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'write_comments','write_case_time','answer_comments','ex_result','test_comments']

    list_display =[ 'case_title','case_precondition', 'case_step', 'case_expected_result','write_comments',
                    'answer_comments'
                    ] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module','test_page','requirement_function','case_priority',
              'case_process_type', 'case_title','case_precondition', 'case_step', 'case_expected_result',
              'write_comments']
    list_filter = ['id','test_project','test_module','test_page','case_priority','case_process_type','case_title','write_comments',]   #定义筛选的字段
    model_icon = 'fa fa-eye'  # 定义图标显示
    ordering = ['id']  # 添加默认排序规则显示排序，根据id正序排序
    # readonly_fields = ['write_case_time','write_user']  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    readonly_fields = ['write_user', 'write_case_time','test_user']  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，

    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    list_editable = ziduan # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project','case_title',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project','case_title',]   #显示数据详情

    # def queryset(self):
    #     qs = super(CopyTestCaseAdmin, self).queryset()
    #     if self.request.user.is_superuser:  # 超级用户可查看所有数据
    #         return qs
    #     else:
    #         return qs.filter(write_user=self.request.user)  # user是Model的write_user字段

    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     """对外键进行设置"""
    #     if db_field.name == 'write_user':
    #         kwargs['initial'] = request.user.id
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(CopyTestCaseAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs
    #     )

    # def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(CopyTestCaseAdmin, self).queryset()   #调用父类
    #     if self.request.user.is_superuser:   #超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(write_user=self.request.user)  #否则只显示本用户数据
    #         return qs   #返回qs
    # def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
    #     #在保存用例的时候统计新加用例项目名字是否新加，模块名字是否新加，以及新加数，以及在用户报告模块中自动新加内容
    #     obj = self.new_obj   #取得当前用例的实例
    #     obj.save()   #保存当前用例
    #
    #     casereports = CaseReport.objects.all()   #获取CaseReport所用内容
    #     casereport_project_name_list =[]
    #     casereport_module_name_list = []
    #     for casereport in casereports:
    #         casereport_project_name_list.append(casereport.test_project)  #将CaseReport中所有项目名保存在一个列表里
    #         casereport_module_name_list.append(casereport.test_module)   #将CaseReport中所有模块名保存在一个列表里
    #
    #     if obj.test_project not in casereport_project_name_list:  #如果新加用例的项目名不在CaseReport项目中，则新加一条数据
    #         newcasereport = CaseReport()
    #         newcasereport.test_project = obj.test_project
    #         newcasereport.test_module =obj.test_module
    #         newcasereport.save()
    #     elif obj.test_module not in casereport_module_name_list:
    #         newcasereport = CaseReport()
    #         newcasereport.test_project = obj.test_project
    #         newcasereport.test_module =obj.test_module
    #         newcasereport.save()
    def save_models(self):   #重载save_models的方法，可以在做了某个动作后，动态重新加载
        #在保存用例的时候统计新加用例项目名字是否新加，模块名字是否新加，以及新加数，以及在用户报告模块中自动新加内容
        obj = self.new_obj   #取得当前用例的实例
        if self.request.user.is_superuser:  # 超级用户则不对编写人做修改
            obj.save()  # 保存当前用例
        else:    #非超级用户会自动保存编写人
            if obj.write_user_id == None:
                user = User.objects.get(username=self.request.user)
                obj.write_user_id = user.id  #保存当前的write_user为用户登录的user
            obj.save()   #保存当前用例


xadmin.site.register(CopyTwoTestCase, CopyTwoTestCaseAdmin) #在xadmin中注册CopyTwoTestCase


class BaseSettings(object):   #全站的配置类, 配置主题
    enable_themes = True  #主题功能,enable_themes=True 表示要使用它的主题功能，xadmin默认是取消掉的
    use_bootswatch = True   #xadmin默认是取消掉的

xadmin.site.register(views.BaseAdminView, BaseSettings)   #注册BaseSettings


class GlobalSettings(object):   ##全站的配置类
    site_title = "测试用例后台管理系统"   #页面左上角的标题名称
    site_footer = "测试网"   #页面底部的文字显示内容
    menu_style = "accordion"  # 将一个app下的内容收起来

xadmin.site.register(views.CommAdminView, GlobalSettings)   #注册GlobalSettings