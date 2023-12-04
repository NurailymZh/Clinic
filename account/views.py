from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, logout

from account.models import CustomUser
from account import forms
from myapp import serializers
# def login(request):
#     form = forms.CustomLoginForm()
#     if request.method == 'POST':
#         form = forms.LoginForm(request = request,data=request.POST)
#         if form.is_valid():
#             username = forms.cleaned_data.get("username")
#             password = forms.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             print("jnnkjnj")
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 print('form', user)
#         else:
#             print('form_in_valid', form)
#     return render(request, 'account/login.html', { 'form': form})

def login(request):
    form=forms.CustomLoginForm()
    msg = []
    if request.method == 'POST':
        form=forms.CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    msg.append("login successful")
                    return redirect('home')
                else:
                    msg.append("disabled account")
            else:
                msg.append("invalid login")

    return render(request, 'account/login.html', context={
        'form': form
    })

def my_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = forms.CustomUserForm()
    if request.method == 'POST':
        print('ddd', request.POST)
        form = forms.CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.save()
            return redirect('login')
        
    return render(request, "account/register.html", { 'form': form})

