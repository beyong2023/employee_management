from django.shortcuts import render, redirect
from app_1.utils.pagination import Pagination
from app_1 import models
from app_1.utils.form import PrettyModelForm, PrettyEditModelForm

""" 靓号 """


def pretty_list(request):
    """ 靓号列表 """
    # for i in range(300):
    #      models.PrettyNum.objects.create(mobile="99999999990", price="99", level="1", status="1")
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    page_object = Pagination(request, queryset)
    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数量
        "page_string": page_object.html()  # 页码
    }
    return render(request, 'pretty_list.html', context)

    # models.PrettyNum.objects.filter(mobile="199999999991", id=12)
    #
    # data_dict = {"mobile": "98888888888", "id": 123)
    # models.PrettyNum.objects.filter(**data_dict)
    #
    # models.PrettyNum.objects.filter(id=2)
    # models.PrettyNum.object.filter(id__gt=12)
    # models.PrettyNum.object.filter(id__gte=12)
    # models.PrettyNum.object.filter(id__lt=12)
    # models.PrettyNum.object.filter(id__lte=12)
    #
    # data_dict = {"id__lte":12}
    # models.PrettyNum.objects.filter(**data_dict)
    #
    # models.PrettyNum.objects.filter(mobile="999")
    # models.PrettyNum.objects.filter(mobile__startswith="1999")
    # models.PrettyNum.objects.filter(mobile__endswith="999")
    # models.PrettyNum.object.filter(mobile__contains="9999")
    #
    # data_dict = {"mobile_contains": "999"}
    # models.PrettyNum.objects.filter(**data_dict)


def pretty_add(request):
    """添加靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    return render(request, 'pretty_add.html', {"form": form})


def pretty_edit(request, nid):
    """编辑靓号"""
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})

    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, nid):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")
