
from django.contrib import admin
from django.urls import path, re_path,include
from . import views

urlpatterns = [
    path('employee/<action>',views.emp,name='employee'),
    path('get_employee/<int:id>',views.get_employee,name='get_employee'),
    path('del_employee/<int:id>',views.del_employee,name='del_employee'),
    path('upd_employee/<int:id>',views.upd_employee,name='upd_employee'),

]
