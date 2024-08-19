from django.shortcuts import redirect, render
from django.contrib import messages
from portfolio.models import Contact,Blog

# Create your views here.
def home(request):
    return render(request,'home.html')
def basic(request):
    return render(request,'basic.html')
def about(request):
    return render(request,'about.html')
def contact(request):

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('phonenumber')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,' Thanks for Contacting us we will get back you soon!')
        return redirect('/contact/')
       

    return render(request,'contact.html')
def resume(request):
    return render(request,'resume.html')
def portfolio(request):
    return render(request,'portfolio.html')
def services(request):
    return render(request,'services.html')
def blog(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request,'blog.html',context)
def custom_blog(request):
    return render(request,'custom_blog.html')
def ecom(request):
    return render(request,'ecom.html')