"""yiniceshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

import xadmin

urlpatterns = [
    path('', xadmin.site.urls),
    # yinics应用url配置
    path('testcase/', include('yinics.urls', namespace='testcase')),  # 配置测试用例url,namespace指明命名空间，用命名空间做限定
    # path('casereport/', include('casereport.urls', namespace='case_report')),  # 配置测试用例url,namespace指明命名空间，用命名空间做限定
    # url(r'^ueditor/',include('DjangoUeditor.urls' ))

    path('ueditor/',include( 'DjangoUeditor.urls' )), #配置富文本相关url  富文本使用-2
]
