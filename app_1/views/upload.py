import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app_1 import models


def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')
    # # POST 请求体中的数据
    # print(request.POST)
    # # FILES 请求发送过来的文件
    # print(request.FILES)
    file_object = request.FILES.get("avatar")
    f = open(file_object.name, mode='wb')
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("...")


from django import forms
from app_1.utils.bootstrap import BootStrapForm
from app_1.utils.bootstrap import BootStrapModelForm


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


class UpModelForm(BootStrapModelForm):
    class Meta:
        model = models.City
        fields = "__all__"


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # print(form.changed_data)
        # print(form.cleaned_data)
        # 1. 读取图片内容， 写入到文件夹中并获取文件的路径
        image_object = form.cleaned_data.get("img")


        # file_path = "app01/static/img/{}".format(image_object.name)
        # file_path = os.path.join("app_1", "static", "img", image_object.name)
        # db_file_path = os.path.join("static", "img", image_object.name)
        media_path = os.path.join("media", image_object.name)

        # file_path = os.path.join("app_1", db_file_path)
        # f = open(file_path, mode="wb")
        f = open(media_path, mode="wb")
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 2. 将图片路径写入到数据库
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            #img=db_file_path,
            img = media_path
        )
        return HttpResponse("...")
    return render(request, 'upload_form.html', {"form": form, "title": title})


def upload_model_form(request):
    title = "ModelForm上传文件"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 字段 + 路径 写入数据库中
        form.save()
        return HttpResponse("成功")
    return render(request, 'upload_form.html', {"form": form, 'title': title})












































