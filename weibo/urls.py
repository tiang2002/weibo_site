from django.urls import path

from . import views

app_name = 'weibo'  # 重点是这一行,避免和其他app的命名空间重合。

urlpatterns = [
    # 例如: /weibo/ <- 该参数已由根urls.py接收，不再传入该二级路由
    path('', views.index, name='index'),
    # path('pie/', views.pie, name='pie'),

    # path()
    # 例如: /polls/5/
]