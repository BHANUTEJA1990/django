from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def tpl_var_demo(request,name):
    template_name="tpl_var_demo.html"
    context={'num':10,'year':2020,'name':name}
    return render(request,template_name,context=context)

def show_static(request):
    template_name="static_demo.html"
    return render(request,template_name)

def tpl_if_demo(request):
    template_name="tpl_if_demo.html"
    context={
        'fruits_list':['apple','orange','grapes',]
    }
    return render(request,template_name,context=context)

def tpl_for_demo(request):
    template_name="tpl_for_demo.html"
    emp={
        'emp_details':[
            {'name':'ABC','id':1000},
            {'name': 'BBC', 'id': 1001},
            {'name': 'CBC', 'id': 1002},
            {'name': 'DBC', 'id': 1003},
            {'name': 'EBC', 'id': 1004},

        ]
    }
    return render(request,template_name,context=emp)

def dtl_cycle_demo(request):
    template_name="dtl_cycle_demo.html"
    context={
       'device_list':["apple","samsung","oppo","htc","nokia","pansonic","sony"]

    }
    return render(request,template_name,context=context)


def dtl_inheritance_demo(request):
    template_name="dtl_child_demo.html"
    context={
       'device_list':["apple","samsung","oppo","htc","nokia","pansonic","sony"]

    }
    return render(request,template_name,context=context)

def dtl_inheritance_demo(request):
    template_name="dtl_inheritance_demo.html"
    context={
        'fruits_list': ['apple', 'orange', 'grapes', ]

    }
    return render(request,template_name,context=context)

def tpl_filters_demo(request):
    template_name="tpl_filters_demo.html"
    context={
        'fruits_list': ['apple', 'orange', 'grapes', ],
        'num_list':[1,2,3,4,5,6,7,8,9],
        'date_time':datetime.now(),
        'past_time':datetime(2002,2,23),
        'number':20,
        'slug': "hghgyu ygy y ty  uy "

    }
    return render(request,template_name,context=context)
def show_home(request):
    template_name="home.html"

    return render(request,template_name)

#

def edit(request ,id):
    template_name="edit.html"
    context={'edit':id}
    return render(request,template_name,context=context)


def delete(request, id):
    template_name="delete.html"
    context={delete(id)}
    return HttpResponse(f"Id to be deleted: {id}")


def delete(request,id):
    template_name="delete.html"
    context={'name':id}
    return render(request,template_name,context=context)