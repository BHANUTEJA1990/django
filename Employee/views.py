from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee


# Create your views here.
def emp(fname, Iname, age, address):
    pass


def emp(request, action):
    if action == "add":
        emp = Employee(fname="rajendra", iname="Tcs", age="30",address='btm bangloor')
        emp.save()
        return HttpResponse(f"employee is added:{emp}")
    elif action == "get":
        template_name = 'employee_demo.html'
        employee_list = Employee.objects.all()
        #print(f"employee_list:{employee_list}")
        context = {"employee_list":employee_list}
        #employee = Employee.objects.filter(age='30').values_list()
       # context = Employee.objects.filter(fname='rajendra').values()
        return render(request, template_name, context=context)
        #emp=Employee.objects.all()


        #employee=Employee.objects.filter(fname__startswith="r");

       # print(f"Employee list:{employee}")

        #employee=Employee.objects.exclude (fname='bhanuteja')
        #print(f"Employee list:{employee}")
       # return HttpResponse(f"Employee will add: {employee} ")

    else:
        return HttpResponse("invalid action.", status=400)


def get_employee(request, id):
    template_name = "employee_get.html"
    employee = Employee.objects.get(id=id)
    context = {'employee': employee}
    return render(request, template_name, context=context)


def del_employee(request, id):
    employee_inst = Employee.objects.get(pk=id)
    employee_inst.delete()
    return redirect('employee', action='get')


def upd_employee(request, id):
    emp_inst = Employee.objects.get(pk=id)
    emp_inst.fname = "new name"
    emp_inst.iname = "new iname"
    emp_inst.save()
    return redirect('employee', action='get')


from django.shortcuts import render

# Create your views here.
