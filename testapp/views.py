from django.shortcuts import render,redirect
from . forms import SignUpForm
from  django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        fm=SignUpForm(request.POST)
        fm.is_valid()
        fm.save()
        messages.success(request,'your Account well be Created success')
    else:
        fm=SignUpForm()
    return render(request,'testapp/registration.html',{'form':fm})
def LoginView(request):
    if not request.user.is_authenticated:
        if request.method== 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pword=fm.cleaned_data['password']
                user=authenticate(username=uname,password=pword)
                if user is not None:
                    login(request,user)
                    return redirect('dashboard')
        else:
            fm = AuthenticationForm()
            return render(request,'testapp/login.html',{'form':fm})
    else:
        return redirect('dashboard')
def DashBoardView(request):
    if request.user.is_authenticated:
        return render(request,'testapp/dashboard.html',{'name':request.user.username})
    else:
        return redirect('Log_In')
def logout_view(request):
    logout(request)
    return redirect('Log_In')
