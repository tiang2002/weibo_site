from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .pie import get_pie_html
import re


def index(request):
    with open('weibo/templates/weibo/pic.txt', 'r') as file:
        chart_pie = file.read()

    return render(request, 'weibo/index.html', {'chart_pie': chart_pie})


def pie(request):
    get_pie_html()

    return render(request, 'weibo/pic.html')
