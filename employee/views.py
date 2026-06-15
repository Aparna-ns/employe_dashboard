from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def user_login(request):

    if request.method=="POST":

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(
            username=username,
            password=password
        )

        if user:
            login(request,user)
            return redirect('dashboard')

    return render(request,'login.html')


@login_required
def dashboard(request):

    employee=Employee.objects.get(user=request.user)

    holidays=Holiday.objects.all()[:5]

    payslips=Payslip.objects.filter(
        employee=employee
    )

    context={

        'employee':employee,
        'holidays':holidays,
        'payslips':payslips

    }

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def leave_apply(request):

    form=LeaveForm()

    if request.method=="POST":

        form=LeaveForm(request.POST)

        if form.is_valid():

            leave=form.save(commit=False)

            leave.employee=Employee.objects.get(
                user=request.user
            )

            leave.save()

            return redirect('dashboard')

    return render(
        request,
        'leave.html',
        {'form':form}
    )


def user_logout(request):

    logout(request)

    return redirect('login')