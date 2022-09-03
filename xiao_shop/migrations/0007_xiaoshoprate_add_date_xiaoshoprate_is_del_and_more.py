# Generated by Django 4.0.3 on 2022-04-09 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xiao_shop', '0006_remove_xiaoshoprate_tag_xiaoshoprate_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiaoshoprate',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='添加时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xiaoshoprate',
            name='is_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='xiaoshoprate',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
