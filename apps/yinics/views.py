from django.shortcuts import render
from django.views.generic import View   #导入View
from django.http import HttpResponse   #导入HttpResponse ，用于指定返回的类型，返回的是json字符串
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger #分页导入包
from django.contrib.auth.models import User #导入引用django默认新建user表的类User
from django.db.models import Q   #导入Q，筛选作为或与用


from .models import TestCase   #导入TestCase
from .forms import TestCaseForm   #导入QSTestCaseForm
from casereport.models import CaseReport   #导入CaseReport





# Create your views here.
class  TestCaseView(View):  #继承View
    """
    测试用例复制编写页面处理
    """
    def get(self,request,testcase_id):
        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            testcase = TestCase.objects.get(id=int(testcase_id))   #获取用例
            return render(request,"testcase.html",{"testcase":testcase, })
        else:
            return render(request,"addcaseError.html")

    def post(self, request,testcase_id):
        username = request.user.username
        testcase_form = TestCaseForm(request.POST)  # 实例化TestCaseFrom()
        testcase = TestCase.objects.get(id=int(testcase_id))  # 获取用例

        if testcase_form.is_valid():  # is_valid()判断是否有错

            testcase_form.save(commit=True)  # 将信息保存到数据库中

            # zj = QSTestCase.objects.all().order_by('-id')[:1][0]   #根据id查询最新的
            zj = TestCase.objects.all().order_by('-write_case_time')[:1][0]  # 根据添加时间查询最新的
            user = User.objects.get(username=username)
            zj.write_user_id = user.id
            zj.save()

            #判断新加的用例的项目名称和模块名称是否是新的，是新的就在CaseReport模块中新加，不是就不加
            casereports_projectandmodule_name_list = []
            casereports = CaseReport.objects.all()  # 获取CaseReport所用内容
            for casereport in casereports:
                casereports_projectandmodule_name_list.append(
                    "%s@#*pap%s" % (casereport.test_project, casereport.test_module))

            newaddtestcase = "%s@#*pap%s" % (zj.test_project, zj.test_module)

            if newaddtestcase not in casereports_projectandmodule_name_list:  # 如果新加用例的项目名不在CaseReport项目中，则新加一条数据
                newcasereport = CaseReport()
                newcasereport.test_project = zj.test_project
                newcasereport.test_module = zj.test_module
                newcasereport.save()

            tesecaseid = zj.id
            # qstesecase_id = int(qstesecase_id) +1
            testcaseadd = TestCase.objects.get(id=int(tesecaseid))  # 获取用例
            return render(request, "testcase.html", {
                "testcase": testcaseadd,
                "sumsg":u"添加测试用例---【{}】---成功,请继续添加".format(testcaseadd.case_title),
            })
        else:
            # return render(request, 'testcase.html', {
            #     "testcase": testcase,
            #     "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
            # })  # 返回页面，回填信息
            return render(request, 'testcaseform.html', {
                "testcase": testcase,
                "testcaseform": testcase_form,
                "errmsg":u"添加失败，请重新添加，添加时请检查各个字段是否填写",
            })  # 返回页面，回填信息


# class  DisplayTestCaseView(View):  #继承View
#     """
#     查看测试用例页面处理
#     """
#     def get(self,request,testcase_id):
#         displaytestcase = TestCase.objects.get(id=int(testcase_id))   #获取用例
#         assocase = displaytestcase.asso_case
#         return render(request,"displaytestcase.html",{
#             "testcase":displaytestcase,
#             "assocase": assocase,
#         })
#
#
# class  MoreTestCaseView(View):  #继承View
#     """
#     查看多对多关联测试用例页面处理
#     """
#     def get(self,request,testcase_id):
#         moretestcase = TestCase.objects.get(id=int(testcase_id))   #获取用例
#         rele_cases = moretestcase.rele_case.all()
#
#         return render(request,"moretestcase.html",{
#             "testcase":moretestcase,
#             "rele_cases": rele_cases,
#         })
#
#
# class  AllTestCaseSiderView(View):  #继承View
#     """
#     查看所有测试用例页面-侧边栏页面处理
#     """
#     def get(self,request):
#
#         sidertestcases = TestCase.objects.all()  #获取用例
#
#         #对测试用例进行分页
#         try:
#             page = request.GET.get('page', 1)     #取第一页
#         except PageNotAnInteger:
#             page = 1                        #取第一页
#         p = Paginator(sidertestcases, 15, request=request)   #自动对all_orgs（获取的所有课程机构的数据）进行分页，每页5个
#         sidertestcases = p.page(page)   #取与页数相对的数据
#         return render(request,"testcasebase.html",{
#             "sidertestcases":sidertestcases,
#         })
#
#
# class  SiderCaseDisplayView(View):  #继承View
#     """
#     查看所有测试用例页面-侧边栏页面的测试用例详情
#     """
#     def get(self,request,testcase_id):
#         sidercasedisplay = TestCase.objects.get(id=int(testcase_id))   #获取用例
#
#         rele_cases = sidercasedisplay.rele_case.all()
#
#         sidertestcases = TestCase.objects.all()  #获取用例
#
#         #对测试用例进行分页
#         try:
#             page = request.GET.get('page',1)     #取第一页
#         except PageNotAnInteger:
#             page = 1                        #取第一页
#         p = Paginator(sidertestcases, 15, request=request)   #自动对all_orgs（获取的所有课程机构的数据）进行分页，每页5个
#         sidertestcases = p.page(page)   #取与页数相对的数据
#         print(page)
#
#
#
#         return render(request,"testcasebase.html",{
#             "sidertestcases": sidertestcases,
#             "testcase":sidercasedisplay,
#             "rele_cases": rele_cases,
#             "page":page,
#
#         })
#
#
# class  SiderCaseDetailsView(View):  #继承View
#     """
#     查看所有测试用例页面-侧边栏页面的测试用例详情
#     """
#     def get(self,request,testcase_id):
#         sidercasedisplay = TestCase.objects.get(id=int(testcase_id))   #获取用例
#
#         rele_cases = sidercasedisplay.rele_case.all()
#
#         return render(request,"testcasebase.html",{
#             "testcase":sidercasedisplay,
#             "rele_cases": rele_cases,
#         })
#     # """
#     # 用户添加咨询   #添加注释
#     # """
#     # def post(self, request):   #此处表单只有一个post请求，表单的请求
#     #     userask_form = UserAskForm(request.POST)   #实例化
#     #     if userask_form.is_valid():   #如果合法
#     #         user_ask = userask_form.save(commit=True)   #commit=True表示提交后直接保存到数据库commit=False表示只是表单提交数据，没有保存到数据库
#     #         return  HttpResponse('{"status":"success"}', content_type='application/json')   #返回json串，正确，返回成功,content_type用来指明字符串的格式,此处指明为json
#     #     else:
#     #         # return HttpResponse("{'status':'fail', 'msg':'添加出错'}", content_type='application/json')
#     #         return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json') #失败，返回失败原因,content_type='application/json'为固定的写法


class  RelaCaseDisplayView(View):  #继承View
    """
    查看所有测试用例页面-侧边栏页面的测试用例详情
    """
    def get(self,request,testcase_id):

        if request.user.username == 'check':
            return render(request, "NoAddCase.html")
        elif request.user.is_active:
            testcase = TestCase.objects.get(id=int(testcase_id))  # 获取用例

            rele_cases = testcase.rele_case.all()

            alltestcases = TestCase.objects.all().order_by("id")  # 获取用例

            #搜索
            search_keywords_test_project = request.GET.get('test_project', "")
            search_keywords_test_module = request.GET.get('test_module', "")
            search_keywords_test_page = request.GET.get('test_page', "")
            search_keywords_case_title = request.GET.get('case_title', "")
            print("-------------------------------------------:",search_keywords_test_project)
            if search_keywords_test_project:
                # 多个字段模糊查询， 括号中的下划线是双下划线，双下划线前是字段名，双下划线后可以是icontains或contains,区别是是否大小写敏感，竖线是或的意思
                alltestcases = alltestcases.filter(Q(test_project__icontains=search_keywords_test_project))
            if search_keywords_test_module:
                alltestcases = alltestcases.filter(Q(test_module__icontains=search_keywords_test_module))
            if search_keywords_test_page:
                alltestcases = alltestcases.filter(Q(test_page__icontains=search_keywords_test_page))
            if search_keywords_case_title:
                alltestcases = alltestcases.filter(Q(case_title__icontains=search_keywords_case_title))



            # 对测试用例进行分页
            try:
                page = request.GET.get('page', 1)  # 取第一页
            except PageNotAnInteger:
                page = 1  # 取第一页
            p = Paginator(alltestcases, 15, request=request)  # 自动对all_orgs（获取的所有课程机构的数据）进行分页，每页25个
            sidertestcases = p.page(page)  # 取与页数相对的数据

            # for sidertestcase in sidertestcases:
            #     if testcase.id ==sidertestcase.id
            #         relacasepage =

            return render(request, "testcasebase.html", {
                "sidertestcases": sidertestcases,
                "testcase": testcase,
                "rele_cases": rele_cases,
                "page": page,
                'search_keywords_test_project':search_keywords_test_project,
                'search_keywords_test_module':search_keywords_test_module,
                'search_keywords_test_page':search_keywords_test_page,
                'search_keywords_case_title':search_keywords_case_title,
            })

        else:
            return render(request,"addcaseError.html")




