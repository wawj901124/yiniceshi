from datetime import datetime   #导入获取时间包

from django.db import models   #导入django的models
from django.contrib.auth.models import User #导入引用django默认新建user表的类User


# Create your models here.
class ProjectProgress(models.Model):
    project_name = models.CharField(max_length=50, default="", verbose_name=u"项目名称",help_text=u"项目名称")
    project_status = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("S0", u"未开始"), ("S1", u"进行中") , ("S3", u"已结束"), ("S4", "阻塞停止")),
                                     default="S0",
                                     verbose_name=u"项目状态")
    project_leader = models.ForeignKey(User, related_name="projectleader", null=True, blank=True, verbose_name=u"项目总监",
                                   on_delete=models.DO_NOTHING)
    project_start_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"项目开始时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    project_end_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"项目结束时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    project_user_time = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2,verbose_name=u"项目历时（以天为单位）")   #定义浮点类型，可以定义总位数（max_digits）和小数点后的位数（decimal_places）,max_digits=4表示整个位数为4位，
                                                                    # decimal_places=2表示小数点后位数为2位

    product_leader = models.ForeignKey(User, related_name="productleader", null=True, blank=True, verbose_name=u"产品总监",
                                   on_delete=models.DO_NOTHING)
    product_staff = models.ManyToManyField(User, related_name="productstaff", null=True, blank=True, verbose_name=u"产品人员")

    requirement_status = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("S0", u"未开始收集"), ("S1", u"收集进行中") , ("S3", u"收集已完毕"), ("S4", "无需求")),
                                     default="S0",
                                     verbose_name=u"需求状态")
    requirement_start_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"需求收集开始时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    requirement_end_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"需求收集结束时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    requirement_user_time = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2,verbose_name=u"需求收集历时（以天为单位）")   #定义浮点类型，可以定义总位数（max_digits）和小数点后的位数（decimal_places）,max_digits=4表示整个位数为4位，
                                                                    # decimal_places=2表示小数点后位数为2位

    develop_leader = models.ForeignKey(User, related_name="developleader", null=True, blank=True, verbose_name=u"开发总监",
                                   on_delete=models.DO_NOTHING)

    develop_staff = models.ManyToManyField(User, related_name="developstaff", null=True, blank=True, verbose_name=u"开发人员")

    develop_status = models.CharField(max_length=10,null=True, blank=True,
                                     choices=(("S0", u"未开始开发"), ("S1", u"开发进行中") , ("S3", u"开发已完毕"), ("S4", "不开发")),
                                     default="S0",
                                     verbose_name=u"开发状态")
    develop_start_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"开发开始时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    develop_end_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"开发结束时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间

    develop_user_time = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2,verbose_name=u"开发历时（以天为单位）")   #定义浮点类型，可以定义总位数（max_digits）和小数点后的位数（decimal_places）,max_digits=4表示整个位数为4位，
                                                                    # decimal_places=2表示小数点后位数为2位

    test_leader = models.ForeignKey(User, related_name="testleader", null=True, blank=True, verbose_name=u"测试总监",
                                       on_delete=models.DO_NOTHING)

    test_staff = models.ManyToManyField(User, related_name="teststaff", null=True, blank=True,
                                           verbose_name=u"测试人员")

    test_status = models.CharField(max_length=10, null=True, blank=True,
                                      choices=(("S0", u"未开始测试"), ("S1", u"测试进行中"), ("S3", u"测试已完毕"), ("S4", "不测试")),
                                      default="S0",
                                      verbose_name=u"测试状态")
    test_start_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"测试开始时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    test_end_time = models.DateTimeField(default="", null=True, blank=True,
                                    verbose_name=u"测试结束时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间
    test_user_time = models.DecimalField(null=True, blank=True,max_digits=4,decimal_places=2,verbose_name=u"测试历时（以天为单位）")   #定义浮点类型，可以定义总位数（max_digits）和小数点后的位数（decimal_places）,max_digits=4表示整个位数为4位，
                                                                    # decimal_places=2表示小数点后位数为2位

    add_time = models.DateTimeField(null=True, blank=True,auto_now_add=True,
                                    verbose_name=u"添加时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间,auto_now_add=True是指定在数据新增时, 自动写入时间
    update_time = models.DateTimeField(null=True, blank=True,auto_now=True,
                                    verbose_name=u"更新时间")  # datetime.now记录实例化时间，datetime.now()记录模型创建时间，auto_now=True是无论新增还是更新数据, 此字段都会更新为当前时间

    class Meta:
        verbose_name = u"项目进度统计"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.project_name

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
