from django.shortcuts import render,redirect
from .forms import RegisterForm, EmployeeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from .models import Employee


# Create your views here.
def register_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            context = {
                'username':username,
                'email':email,
            }
            form = RegisterForm(request.POST)
            if form.is_valid():
                user_permisssion = form.save()
                group = Group.objects.get(name='Viewer')
                user_permisssion.groups.add(group)
                messages.success(request,"User created successfully")
                return redirect('/login-user')
            else:
                messages.error(request,"Validation didn't match")
                return render(request, 'app/register.html', context)
        else:
            form = RegisterForm()
            
        return render(request, 'app/register.html')
    else:
        return redirect('/')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            context = {
                'username':username,
            }
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.error(request,'Username and Password are Incorrect')
                    return render(request, 'app/login.html', context)
            else:
                messages.error(request,'Fill the input fields')
                return render(request, 'app/login.html', context)

        return render(request, 'app/login.html')
    else:
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def index(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp,
    }
    return render(request, 'app/index.html',context)

def add_employee(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form,
    }
    return render(request, 'app/add_employee.html',context)

def update_employee(request,pk):
    emp = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=emp) #instace = emp vanesi emp ko name,email contact and salary ko values haru aayo haina????
    if request.method =="POST":
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            messages.info(request,'Employee Updated successfully')
            return redirect('/')
    context = {
        'emp':emp,
        'form':form,
    }
    return render(request, 'app/update_employee.html',context )

def delete_employee(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == "POST":
        emp.delete()
        return redirect('/')
    context ={
        'emp':emp,
    }
    return render(request,'app/delete_employee.html',context)