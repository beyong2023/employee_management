# Generated by Django 4.1.5 on 2023-01-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0003_alter_department_title_alter_userinfo_depart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="create_time",
            field=models.DateField(verbose_name="入职时间"),
        ),
    ]
