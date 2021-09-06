"""dj_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 固定网页
    path('page1', views.page1),

    # re_path自定义网页
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w*)/(?P<y>\d{1,2})$', views.cal_view),

    # 自定义匹配网页：http://127.0.0.1:8000/整数/操作符/整数        path函数：int和str类型
    path('<int:num1>/<str:calculate_method>/<int:num2>', views.calculate_total),

    re_path(r'birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2}$)', views.view_birthday1),
    re_path(r'birthday/(?P<month>\d{1,2})/(?P<year>\d{4})/(?P<day>\d{1,2}$)', views.view_birthday2)

]
