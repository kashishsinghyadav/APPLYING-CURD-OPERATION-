from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from loginuser.models import Emp,Position
from .forms import EmployeeForm

def employee_list(request):
    context = {'employee_list': Emp.objects.all()}
    return render(request, "list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Emp.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Emp.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request,id):
    employee = Emp.objects.get(pk=id)
    employee.delete()
    return redirect('/list')