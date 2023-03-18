"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path,include
from . import views

urlpatterns = [
    path('tpl_var_demo/<name>',views.tpl_var_demo,name="tpl_var_demo"),
    path('tpl_if_demo', views.tpl_if_demo, name="tpl_if_demo"),
    path('tpl_for_demo', views.tpl_for_demo, name="tpl_for_demo"),
    path('dtl_cycle_demo', views.dtl_cycle_demo, name="dtl_cycle_demo"),
    path('dtl_inheritance_demo', views.dtl_inheritance_demo, name="dtl_inheritance_demo"),
    path('tpl_filters_demo',views.tpl_filters_demo,name="tpl_filters_demo"),
    path('show_home', views.show_home, name="show_home"),
    path('show_static',views.show_static,name="show_static"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('devapp/',include('devapp.urls')),
    #path('starbuck/',include('starbuck.urls')),
   # path('index/',views.show_text,name='index'),
    #path('inc/<int:num>', views.inc_by_ten,name='inc_by_ten'),
    #path('add/<int:num1>/<int:num2>', views.add,name='add'),

    #re_path('year/(?P<year>[0-9]{4})/', views.show_year,name='show_year'),
    #re_path(('par'),views.par,name='age')
]
