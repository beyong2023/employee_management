from django.shortcuts import render, redirect
from django.http import JsonResponse


def chart_list(request):
    return render(request, "chart_list.html")


def chart_bar(request):
    """ 构造柱状图的数据 """
    legend = ['kkk', 'hhh']
    series_list = [
        {
            "name": 'kkk',
            "type": 'bar',
            "data": [15, 28, 36, 10, 100]
        },
        {
            "name": 'hhh',
            "type": 'bar',
            "data": [15, 28, 36, 10, 100]
        },
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月']
    result = {
        "status": True,
        "data": {
            'legend': legend,
            'series_list': series_list,
            'x_axis': x_axis,
        }
    }
    return JsonResponse(result)


def chart_pie(request):
    db_data_list = [
        {"value": 1111, "name": "IT部门"},
        {"value": 888, "name":"运营"},
        {"value": 999, "name":"新媒体"}
    ]
    result = {
        "status": True,
        "data": db_data_list,
    }
    return JsonResponse(result)


def high_charts(request):
    return render(request, "chart_high_charts.html")












































