# Generated by Django 2.0.5 on 2019-07-17 14:48

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yinics', '0008_auto_20190717_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='write_comments',
            field=DjangoUeditor.models.UEditorField(blank=True, null=True, verbose_name='编写备注'),
        ),
    ]
