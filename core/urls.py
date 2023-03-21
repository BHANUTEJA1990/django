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
from devapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('devapp/',include('devapp.urls')),
    path('starbuck/',include('starbuck.urls')),
    path('movie/',include('movie.urls')),
    path('calapp/',include('calapp.urls')),
    path('Employee/',include('Employee.urls')),


   # path('index/',views.show_text,name='index'),
    #path('inc/<int:num>', views.inc_by_ten,name='inc_by_ten'),
    #path('add/<int:num1>/<int:num2>', views.add,name='add'),

    #re_path('year/(?P<year>[0-9]{4})/', views.show_year,name='show_year'),
    #re_path(('par'),views.par,name='age')
]
