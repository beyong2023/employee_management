from django import forms
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from app_1.utils.bootstrap import BootStrapModelForm
from app_1 import models


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]

    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data["mobile"]
    #
    #     if len(txt_mobile) != 11:
    #         raise ValidationError("格式错误")
    #     return txt_mobile
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exits = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exits:
            raise ValidationError("手机号已经存在")
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exits = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exits:
            raise ValidationError("手机号已经存在")
        return txt_mobile