from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.


def show_text(request):
    resp="<h2>welcome to the django course!!!</h2>"
    return HttpResponse(resp)

def show_index(request: object):
    templates="show_index.html"
    return render(request,templates)

def rd_demo(request):
    #return redirect('show_index')
    return redirect("inc_by_ten",num=50000)

def inc_by_ten(request, num):
    print(f"the given number is {num}")
    print(f"the given path parameter type is {type(num)}")
    res=num+10000
    resp=f"<h2>welcome to the dejango class it very difficult!!! result ={res}"
    return HttpResponse(resp)


def show_year(request, year):
    resp=f"<h2>year={year}</h2>"
    print(f"")
    return HttpResponse(resp)

def par(reqest,age):
    resp=f"<h2>your age={age}</h2>"
    print(f"")
    return HttpResponse(resps)

def add(reqest,num1,num2):
    print(f'the given number is {num1}')
    print(f"fthe given number is {num2}")
    res=num1+num2
    resp=f"<h1>hi task is done result={res}</h>"
    return HttpResponse(resp)