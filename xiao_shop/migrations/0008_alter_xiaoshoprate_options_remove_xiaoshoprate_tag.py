# Generated by Django 4.1 on 2022-09-03 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xiao_shop', '0007_xiaoshoprate_add_date_xiaoshoprate_is_del_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xiaoshoprate',
            options={'ordering': ['-add_date']},
        ),
    ]