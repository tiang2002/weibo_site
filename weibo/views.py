import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .pie import get_pie_html
import re
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))


def index(request):
    # with open('weibo/templates/weibo/pic.txt', 'r') as file:
    #     chart_pie = file.read()
    header, num = get_pie_html()
    header = json.dumps(header)
    num = json.dumps(num)
    with open(PROJECT_ROOT + r'/weibo/templates/weibo/css/style.css', 'r', encoding='utf-8') as file:
        css = file.read()
    with open(PROJECT_ROOT + r'/weibo/templates/weibo/js/echarts.min.js', 'r', encoding='utf-8') as file:
        js = file.read()

    return render(request, 'weibo/index.html', locals())


def pie(request):
    # get_pie_html()

    return render(request, 'weibo/pic.html')
