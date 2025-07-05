from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')
    

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('num1')
        password = request.POST.get('num2')
        conform = request.POST.get('num3')

        if password != conform:
            return render(request,'register.html',{'result':'ERROR'})
        if User.objects.filter(username=username).exists():
            return render(request,'register.html',{'result':'Username already exists'})

        user = User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request,'register.html')
def home(request):
    result=None
    if request.method=="POST":
        a=int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        o=request.POST.get('op')
        if o=='add':
            result=a+b
            return redirect('hello',result)
       #return render(request,'home.html',{'result':result})
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})
def logoutpage(request):
    logout(request)
    return redirect('login')