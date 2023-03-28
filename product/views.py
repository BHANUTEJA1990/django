from django.shortcuts import render
from .forms import Productform

# Create your views here.
def add_product(request):
    template_name="add_product.html"
    if request.method =="POST":
        print(f"POST data:{request.POST}")
        pf=Productform(request.POST)
        if pf.is_valid():
            name=pf.cleaned_data['name']
            price=pf.cleaned_data['price']
            email=pf.cleaned_data['email']
    else:
        pf=Productform()

    context={'form':pf}
    return render(request,template_name,context=context)