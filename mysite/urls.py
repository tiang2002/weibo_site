from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('weibo/', include('weibo.urls')),
    path('control/', admin.site.urls),
]
