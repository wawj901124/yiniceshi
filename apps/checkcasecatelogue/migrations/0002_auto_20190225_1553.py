# Generated by Django 2.0.5 on 2019-02-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkcasecatelogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseCatelogueCopyThree',
            fields=[
            ],
            options={
                'verbose_name': '项目目录',
                'verbose_name_plural': '项目目录',
                'proxy': True,
                'indexes': [],
            },
            bases=('checkcasecatelogue.casecatelogue',),
        ),
        migrations.CreateModel(
            name='CaseCatelogueCopyTwo',
            fields=[
            ],
            options={
                'verbose_name': '项目模块目录',
                'verbose_name_plural': '项目模块目录',
                'proxy': True,
                'indexes': [],
            },
            bases=('checkcasecatelogue.casecatelogue',),
        ),
        migrations.AlterModelOptions(
            name='casecatelogue',
            options={'verbose_name': '项目模块页面目录', 'verbose_name_plural': '项目模块页面目录'},
        ),
        migrations.AddField(
            model_name='casecatelogue',
            name='is_repeat_model',
            field=models.BooleanField(default=True, help_text='是否重复模块', verbose_name='是否重复模块'),
        ),
        migrations.AlterField(
            model_name='casecatelogue',
            name='is_repeat',
            field=models.BooleanField(default=True, help_text='是否重复项目', verbose_name='是否重复项目'),
        ),
    ]
