from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def add(reqest,num1,num2):
    print(f'the given number is {num1}')
    print(f"fthe given number is {num2}")
    res=num1+num2
    resp=f"<h1>hi task of add is done result={res}</h>"
    return HttpResponse(resp)

def sub(reqest,num1,num2):
    print(f'the given number is {num1}')
    print(f"fthe given number is {num2}")
    res=num1-num2
    resp=f"<h1>hi task of sub is done result={res}</h>"
    return HttpResponse(resp)
def multi(reqest,num1,num2):
    print(f'the given number is {num1}')
    print(f"fthe given number is {num2}")
    res=num1*num2
    resp=f"<h1>hi task of multiplication is done result={res}</h>"
    return HttpResponse(resp)
def div(reqest,num1,num2):
    print(f'the given number is {num1}')
    print(f"fthe given number is {num2}")
    res=num1/num2
    resp=f"<h1>hi task of division is done result={res}</h>"
    return HttpResponse(resp)

def show_image(request):
    template_name="show_image.html"
    return render(request,template_name)

