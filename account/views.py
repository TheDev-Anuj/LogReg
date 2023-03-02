from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'account/signup.html', {'form':fm})


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data.get('username')
                upass = fm.cleaned_data.get('password')
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request, 'account/signin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/home/')


def Home(request):
    if request.user.is_authenticated:
        return render(request, 'account\home.html')
    else:
        return HttpResponseRedirect('/signin/')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')    
