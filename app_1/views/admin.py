from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from app_1 import models
from app_1.utils import pagination

from django import forms
from app_1.utils.bootstrap import BootStrapModelForm
from app_1.utils.encrypt import md5
from django.http import HttpResponse


def admin_list(request):
    """ 管理员列表 """
    # info_dict = request.session["info"]
    # 构造搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = pagination.Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data
    }
    return render(request, 'admin_list.html', context)


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 此返回什么，以后保存什么到数据库
        return confirm


def admin_add(request):
    """ 添加管理员 """
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change_add.html', {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change_add.html', {'form': form, "title": title})


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        exits = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exits:
            raise ValidationError("不能和以前的密码一致")
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 此返回什么，以后保存什么到数据库
        return confirm


def admin_edit(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect("/admin/list/")
    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change_add.html', {"form": form, "title": title})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change_add.html', {"form": form, "title": title})


def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/admin/list/")
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change_add.html', {"form": form, "title": title})
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, 'change_add.html', {"form": form, "title": title})

























