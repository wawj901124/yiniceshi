from django.contrib.auth.models import User #导入引用django默认新建user表的类User

import xadmin
from xadmin import views   #导入xadmin中的views,用于和 BaseSettings类绑定


from .models import CaseCatelogue,CaseCatelogueCopyTwo,CaseCatelogueCopyThree


class CaseCatelogueAdmin(object):
    ziduan = ['test_project','test_module','test_page','is_repeat','is_repeat_model','add_time']


    list_display =['id','test_project','test_module','test_page','goto_case_page_total_nums',
                   'and_all_projectandmoduleandpage_name'] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module','test_page',]
    list_filter = ['test_project','test_module','test_page',]   #定义筛选的字段
    model_icon = 'fa fa-eye'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project',]   #显示数据详情

    #设置空值显示
    # empty_value_display = "无相关内容"  #没用，不生效

    # #设置wirte_user字段内容为登录的用户名
    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     """对外键进行设置"""
    #     if db_field.name == 'wirte_user':
    #         kwargs['initial'] = request.user.id
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs
    #     )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'writeuser':
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_readonly_fields(self,request, obj=None):
    #     if obj is not None:
    #         return self.readonly_fields + ('writeuser',)
    #     return self.readonly_fields

    # def add_view(self, request, form_url="", extra_context=None):
    #     data = request.GET
    #     data['wirte_user'] = request.user
    #     request.GET = data
    #     return super(TestCaseAdmin, self).add_view(request, form_url="", extra_context=extra_context)

    # def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(TestCaseAdmin, self).queryset()   #调用父类
    #     if self.request.user.is_superuser:   #超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(wirte_user=self.request.user)  #否则只显示本用户数据
    #         return qs   #返回qs

xadmin.site.register(CaseCatelogue, CaseCatelogueAdmin) #在xadmin中注册CaseCatelogue


class CaseCatelogueCopyTwoAdmin(object):
    ziduan = ['test_project', 'test_module', 'test_page', 'is_repeat', 'is_repeat_model', 'add_time']


    list_display =['test_project','test_module','set_is_repeat_model','goto_page_total_nums','goto_case_model_total_nums'] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module']
    list_filter = ['test_project','test_module', 'is_repeat', 'is_repeat_model']   #定义筛选的字段
    model_icon = 'fa fa-eye'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project',]   #显示数据详情

    #设置空值显示
    # empty_value_display = "无相关内容"  #没用，不生效

    # #设置wirte_user字段内容为登录的用户名
    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     """对外键进行设置"""
    #     if db_field.name == 'wirte_user':
    #         kwargs['initial'] = request.user.id
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs
    #     )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'writeuser':
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_readonly_fields(self,request, obj=None):
    #     if obj is not None:
    #         return self.readonly_fields + ('writeuser',)
    #     return self.readonly_fields

    # def add_view(self, request, form_url="", extra_context=None):
    #     data = request.GET
    #     data['wirte_user'] = request.user
    #     request.GET = data
    #     return super(TestCaseAdmin, self).add_view(request, form_url="", extra_context=extra_context)

    # def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(TestCaseAdmin, self).queryset()   #调用父类
    #     if self.request.user.is_superuser:   #超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(wirte_user=self.request.user)  #否则只显示本用户数据
    #         return qs   #返回qs
    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(CaseCatelogueCopyTwoAdmin,self).queryset()   #调用父类
        qs = qs.filter(is_repeat_model='0')  #只过滤显示不重复的数据
        return qs   #返回qs

xadmin.site.register(CaseCatelogueCopyTwo, CaseCatelogueCopyTwoAdmin) #在xadmin中注册CaseCatelogueCopyTwo


class CaseCatelogueCopyThreeAdmin(object):
    ziduan = ['test_project', 'test_module', 'test_page', 'is_repeat', 'is_repeat_model', 'add_time']


    list_display =['test_project','set_is_repeat','goto_model_total_nums','goto_case_project_total_nums'] #定义显示的字段

    # list_display =[ 'test_project','test_module',
    #                 'case_title',
    #           ] #定义显示的字段
    search_fields = ['test_project','test_module']
    list_filter = ['test_project','test_module','is_repeat', 'is_repeat_model']   #定义筛选的字段
    model_icon = 'fa fa-eye'  # 定义图标显示
    ordering = ['-add_time']  # 添加默认排序规则显示排序，根据添加时间倒序排序
    readonly_fields = ziduan  # 设置某些字段为只为可读  #设置了readonly_fields，再设置exclude，exclude对该字段无效，
    # exclude = ['case_step']  # 设置某些字段为不显示，即隐藏  #readonly_fields和exclude设置会有冲突
    # inlines = [TestCaseInline]  # inlines配和TestCaseInline使用，可以直接在项目页面添加测试用例#只能做一层嵌套，不能进行两层嵌套
    # list_editable = ziduan   # 可以在列表页对字段进行编辑
    refresh_times = [3, 5]  # 对列表页进行定时刷新,配置了3秒和5秒，可以从中选择一个
    list_per_page = 50   #每页设置50条数据，默认每页展示100条数据
    # fk_fields = ['test_project_id',]  #设置显示外键字段，未生效
    list_display_links = ['test_project',]   #设置点击链接进入编辑页面的字段
    # date_hierarchy = 'add_time'   #详细时间分层筛选，未生效
    show_detail_fields = ['test_project',]   #显示数据详情
    #设置空值显示
    # empty_value_display = "无相关内容"  #没用，不生效

    # #设置wirte_user字段内容为登录的用户名
    # def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    #     """对外键进行设置"""
    #     if db_field.name == 'wirte_user':
    #         kwargs['initial'] = request.user.id
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(
    #         db_field, request, **kwargs
    #     )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'writeuser':
    #         kwargs['queryset'] = User.objects.filter(username=request.user.username)
    #     return super(TestCaseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # def get_readonly_fields(self,request, obj=None):
    #     if obj is not None:
    #         return self.readonly_fields + ('writeuser',)
    #     return self.readonly_fields

    # def add_view(self, request, form_url="", extra_context=None):
    #     data = request.GET
    #     data['wirte_user'] = request.user
    #     request.GET = data
    #     return super(TestCaseAdmin, self).add_view(request, form_url="", extra_context=extra_context)

    # def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
    #     qs = super(TestCaseAdmin, self).queryset()   #调用父类
    #     if self.request.user.is_superuser:   #超级用户可查看所有数据
    #         return qs
    #     else:
    #         qs = qs.filter(wirte_user=self.request.user)  #否则只显示本用户数据
    #         return qs   #返回qs
    def queryset(self):   #重载queryset方法，用来做到不同的admin取出的数据不同
        qs = super(CaseCatelogueCopyThreeAdmin,self).queryset()   #调用父类
        qs = qs.filter(is_repeat="0")  #只过滤显示不重复的数据
        return qs   #返回qs


xadmin.site.register(CaseCatelogueCopyThree, CaseCatelogueCopyThreeAdmin) #在xadmin中注册CaseCatelogueCopyThree