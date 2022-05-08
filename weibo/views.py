import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .pie import get_pie_html
import re
import os, csv

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))


def index(request):
    # with open('weibo/templates/weibo/pic.txt', 'r') as file:
    #     chart_pie = file.read()
    header, num = get_pie_html()
    header = json.dumps(header)
    num = json.dumps(num)
    points = [[0, 1], [1, 2], [3, 1]]
    with open(PROJECT_ROOT + r'/weibo/templates/weibo/css/weibo_site.css', 'r', encoding='utf-8') as file:
        css = file.read()
    # with open(PROJECT_ROOT + r'/weibo/templates/weibo/js/echarts.min.js', 'r', encoding='utf-8') as file:
    #     js = file.read()

    return render(request, 'weibo/index.html', locals())


def china(request):
    points = [[0, 1], [1, 2], [3, 1]]
    with open(PROJECT_ROOT + r'/weibo/templates/weibo/css/weibo_site.css', 'r', encoding='utf-8') as file:
        css = file.read()
    return render(request, 'weibo/china.html', locals())


def points(request):
    ids = []
    with open(PROJECT_ROOT + r'/weibo/all_id_list.csv') as file:
        reader = csv.reader(file)
        for each in reader:
            ids.append(each[0])
    relations = []
    with open(PROJECT_ROOT + r'/weibo/weibo_forward_list6.csv') as file:
        reader = csv.reader(file)
        reader.__next__()
        for each in reader:
            relations.append(each)
    with open(PROJECT_ROOT + r'/weibo/templates/weibo/css/weibo_site.css', 'r', encoding='utf-8') as file:
        css = file.read()
    return render(request, 'weibo/points.html', locals())


def pie(request):
    # get_pie_html()

    return render(request, 'weibo/pic.html')
