
#mot de passe python2020 name project
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def home(request):
   
    
    return render(request,'lists/home.html')  
def update(request,pk):
    item=tunis.objects.get(id=pk) 
    form=Form(instance=item)
    if request.method=='POST':
        form=Form(request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('/') 
    return render(request,'lists/update.html',{'form':form,'item':item})   
def delete(request,pk):
    item=tunis.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('/')

    return render(request,'lists/delete.html',{'item':item})
def stat(request): 
    tests=tunis.objects.all().order_by('-age')[:30]
   
    
    return render(request,'lists/stat.html',{"tests":tests})
def admi(request):
    return render(request,'lists/admi.html')
def list(request):
    
    tests=tunis.objects.all().order_by('-age')
    form=Form()
    
    if request.method=='POST':
        form=Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/admi/list') 
    return render(request,'lists/list.html',{'form':form,'tests':tests})    

def adm(request):
    return render(request,'registration/login.html')