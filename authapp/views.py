from django.shortcuts import render,redirect
from django.contrib.auth.models  import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def signup(request):

    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_conform_password=request.POST.get('pass2')
        if get_password!=get_conform_password:
            messages.info(request,'Password does not match')
            return redirect('/auth/signup/')
        try:
            if User.objects.filter(username=get_email).exists():
               messages.warning(request,'This Email is already taken')
               return redirect('/auth/signup/')
        except User.DoesNotExist:
            pass

        my_user=User.objects.create_user(get_email,get_email,get_password)
        my_user.save()
        messages.success(request,'created successfully')
        return redirect('/auth/login/')  
    return render(request,'signup.html')

def h_login(request):

    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        my_user=authenticate(username=get_email,password=get_password)
    
        if my_user is not None:
            login(request,my_user)
            messages.success(request,'log in success')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')

    return render(request,'login.html')
def h_logout(request):

    logout(request)
    messages.success(request,'logout success')
    return redirect('/auth/login/')

    return render(request,'logout.html')
