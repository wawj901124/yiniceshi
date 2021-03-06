# Generated by Django 2.0.5 on 2019-04-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yinics', '0004_testcase_answer_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='case_priority',
            field=models.CharField(blank=True, choices=[('P0', '流程用例'), ('P1', '系统的重要功能用例'), ('P2', '系统的一般功能用例'), ('P3', '极低级别的用例')], default='P1', max_length=10, null=True, verbose_name='用例优先级'),
        ),
    ]
