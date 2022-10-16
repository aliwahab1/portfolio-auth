from multiprocessing import context
from venv import create
from django.shortcuts import render, redirect
from itertools import product
from django.shortcuts import render
from .models import Product
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def shop(request):
    product=Product.objects.all()
    context={'products':products}
    return render(request, 'items/flowerbay.html', context)


def registrationPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_date.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

        context = {'form' : form}
        return render (request, 'item/registration.html', context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pasword')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('shop')

        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'items/login.html')