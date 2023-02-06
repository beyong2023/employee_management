# Generated by Django 4.1.5 on 2023-02-04 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0007_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("oid", models.CharField(max_length=64, verbose_name="订单号")),
                ("title", models.CharField(max_length=32, verbose_name="名称")),
                ("price", models.IntegerField(verbose_name="价格")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "待支付"), (2, "已支付")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_1.admin",
                        verbose_name="管理员",
                    ),
                ),
            ],
        ),
    ]
