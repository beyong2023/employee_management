from django.shortcuts import render
from app_1 import models

from django import forms
from app_1.utils.bootstrap import BootStrapForm
from app_1.utils.bootstrap import BootStrapModelForm
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app_1 import models


def city_list(request):
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {"queryset": queryset})


class UpModelForm(BootStrapModelForm):
    class Meta:
        model = models.City
        fields = "__all__"


def city_add(request):
    title = "新建城市"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, 'title': title})

    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 字段 + 路径 写入数据库中
        form.save()
        return redirect("/city/list/")
    return render(request, 'upload_form.html', {"form": form, 'title': title})

















