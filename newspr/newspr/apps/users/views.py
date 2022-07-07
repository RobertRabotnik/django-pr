from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from users.forms import *
from users.models import *
# Create your views here.

def users(request):
    return HttpResponse()


@login_required(login_url='users:login')
def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('blog:home_page')
    else:
        return render(request,'users/logout.html')

@login_required(login_url='users:login')
def account(request):
    request_user = CustomUser.objects.get(id=request.user.id)
    return render(request,'users/account.html',context={'request_user':request_user})

def register(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = UserRegisterForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                return redirect('blog:home_page')
            return render(request,'users/register.html',context={'form':form})
        else:
            form = UserRegisterForm()
            return render(request,'users/register.html',context={'form':form})
    else:
        return redirect('blog:home_page')

def login_user(request):
    if not request.user.is_authenticated:
        if request.POST:
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('blog:home_page')
            return render(request,'users/login.html',context={'form':form})
        else:
            form = UserLoginForm()
            return render(request,'users/login.html',context={'form':form})
    else:
        return redirect('blog:home_page')
            