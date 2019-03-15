# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/5/15 18:21'
from django.urls import  path

# from .views import TestCaseView, DisplayTestCaseView,MoreTestCaseView,AllTestCaseSiderView,SiderCaseDisplayView,SiderCaseDetailsView   #导入TestCaseView
from .views import TestCaseView, RelaCaseDisplayView   #导入TestCaseView


urlpatterns = [
    #相同参数的路径名一定不能一样。比如copy/<path:testcase_id>/与<path:testcase_id>/不能并列存在
    path('copy/<path:testcase_id>/', TestCaseView.as_view(), name="test_case_id"),  # 配置复制新增测试用例url,namespace指明命名空间，用命名空间做限定
    # path('display/<path:testcase_id>/', DisplayTestCaseView.as_view(), name="display_test_case_id"),  # 配置查看测试用例url,namespace指明命名空间，用命名空间做限定
    # path('more/<path:testcase_id>/', MoreTestCaseView .as_view(), name="more_test_case_id"),  # 配置查看测试用例url,namespace指明命名空间，用命名空间做限定
    # path('sider/', AllTestCaseSiderView.as_view(), name="sider_test_case"),  # 配置查看所有测试用例url
    #
    # path('sidercasedisplay/<path:testcase_id>/', SiderCaseDisplayView.as_view(), name="sider_case_display"),  # 配置查看边栏测试用例详情
    # path('sidercasedetails/<path:testcase_id>/', SiderCaseDetailsView.as_view(), name="sider_case_details"),  # 配置查看边栏测试用例详情
    # path('add_ask/', AddUserAskView.as_view(), name="add_ask"),  # 配置课程列表页面的访问路径
    #path('testcase/', OrgView.as_view(), name="test_case"),  # 配置课程列表页面的访问路径
    path('rela/<path:testcase_id>/', RelaCaseDisplayView.as_view(), name="rela_case"),  # 配置相关用例的新路径
]

app_name = 'test'