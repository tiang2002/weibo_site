from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .pie import get_pie_html


def index(request):
    return render(request, 'weibo/index.html')


def pie(request):
    get_pie_html()
    return render(request, 'weibo/pic.html')
