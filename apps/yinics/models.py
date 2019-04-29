from datetime import datetime   #导入获取时间包

from django.db import models   #导入django的models
from django.contrib.auth.models import User #导入引用django默认新建user表的类User


# Create your models here.
class TestCase(models.Model):
    test_project = models.CharField(max_length=50, default="", verbose_name=u"测试项目")
    test_module = models.CharField(max_length=50,default="", verbose_name=u"测试模块")
    test_page = models.CharField(max_length=50, default="", verbose_name=u"测试页面")
    requirement_function = models.TextField(default="",verbose_name=u"功能点")
    case_priority = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("P0", u"流程用例"), ("P1", u"系统的重要功能用例") , ("P2", u"系统的一般功能用例"), ("P3", "极低级别的用例")),
                                     default="P1",
                                     verbose_name=u"用例优先级")
    case_process_type = models.CharField(max_length=10,null=True, blank=True,
                                        choices=(("normal", u"正常流"), ("unusual", u"异常流")),
                                        default="normal",
                                        verbose_name=u"流程类型")
    # asso_case = models.ForeignKey('self',default="",null=True, blank=True, verbose_name=u"关联用例",on_delete=models.CASCADE)
    rele_case = models.ManyToManyField('self', default="", null=True, blank=True, verbose_name=u"关联的用例")
    case_title = models.CharField(max_length=50,verbose_name=u"测试用例_名称")
    case_precondition = models.TextField(default="",null=True, blank=True,verbose_name=u"测试用例_前置条件")
    case_step  = models.TextField(default="",verbose_name=u"测试用例_操作步骤")
    case_expected_result = models.TextField(default="", verbose_name=u"测试用例_预期结果")
    write_comments = models.TextField(default=u"编写备注", null=True, blank=True,verbose_name=u"编写备注")
    answer_comments = models.TextField(default=u"问题答复", null=True, blank=True, verbose_name=u"问题答复")
    write_user = models.ForeignKey(User,related_name="writeuser",null=True, blank=True, verbose_name=u"编写人员", on_delete=models.PROTECT)
    # wirte_user = models.CharField(max_length=50, null=True, blank=True, default="",verbose_name=u"编写人员")

    write_case_time = models.DateTimeField(default=datetime.now, null=True, blank=True,
                                    verbose_name=u"编写用例时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    ex_result = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("pass", u"通过"), ("fail", u"失败") , ("block", u"锁定"), ("na", "未执行")),
                                     default="na",
                                     verbose_name=u"测试结果")
    test_comments = models.TextField(default=u"测试备注", null=True, blank=True,verbose_name=u"测试备注")
    test_user = models.ForeignKey(User, related_name="testuser", null=True, blank=True, verbose_name=u"执行人员",
                                   on_delete=models.PROTECT)
    class Meta:
        verbose_name = u"编写测试用例"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.case_title

    def go_to(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        return mark_safe("<a href='http://ynqbsh.com:8000/testcase/copy/{}/'>复制新加</a>".format(self.id))
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_to.short_description = u"复制新加"   #为go_to函数名个名字

    # def go_display(self):   #定义点击后跳转到某一个地方（可以加html代码）
    #     from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
    #     return mark_safe("<a href='http://ynqbsh.com:8000/testcase/display/{}/'>关联用例查看</a>".format(self.asso_case.id))
    #     # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)
    #
    # go_display.short_description = u"关联用例查看"   #为go_to函数名个名字

    def go_more(self):   #定义点击后跳转到某一个地方（可以加html代码）
        from django.utils.safestring import mark_safe   #调用mark_safe这个函数，django可以显示成一个文本，而不是html代码
        if self.rele_case.all().count() > 0:
            return mark_safe("<a href='http://ynqbsh.com:8000/testcase/rela/{}/'>关联的用例</a>".format(self.id))
        else:
            return mark_safe("<p>无关联用例</p>")
        # return  "<a href='http://192.168.212.194:9002/testcase/{}/'>跳转</a>".format(self.id)

    go_more.short_description = u"关联的用例"   #为go_to函数名个名字


class CopyTestCase(TestCase):
    class Meta:
        verbose_name = u"执行测试用例"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表
                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.case_title


class CopyTwoTestCase(TestCase):
    class Meta:
        verbose_name = u"查看测试用例"
        verbose_name_plural = verbose_name
        proxy = True  #将proxy设置为True,不会再生成一张表，如果不设置为True,就会再生成一张表
                        #将proxy设置为True,不会再生成一张表，同时具有model的属性

    def __str__(self):
        return self.case_title