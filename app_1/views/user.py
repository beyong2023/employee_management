from django.shortcuts import render, redirect
from app_1.utils.pagination import Pagination
from app_1 import models
from app_1.utils.form import UserModelForm

""" 用户 """


def user_list(request):
    """用户列表"""
    queryset = models.UserInfo.objects.all()
    page_object = Pagination(request, queryset, page_size=2)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "user_list.html", context)


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        content = {
            'gender_choice': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, "user_add.html", content)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("ac")
    ctime = request.POST.get("ctime")
    depart_id = request.POST.get("dp")
    gender_id = request.POST.get("gd")
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   depart_id=depart_id, gender=gender_id)
    return redirect("/user/list/")


def user_model_form_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_form_model_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    else:
        # print(form.errors)
        return render(request, 'user_form_model_add.html', {"form": form})


def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {"form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")