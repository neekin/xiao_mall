# Generated by Django 4.0.3 on 2022-04-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiao_shop', '0005_xiaoshoprate_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiaoshoprate',
            name='comment',
            field=models.CharField(default=1, max_length=300, verbose_name='评价'),
            preserve_default=False,
        ),
    ]