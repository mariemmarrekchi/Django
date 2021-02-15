from django.shortcuts import render,redirect

from django import forms

class FormLogin(forms.Form):
    username=forms.CharField(label=("Username"),required=True)
    password=forms.CharField(label=("Password"),widget=forms.PasswordInput,required=True)
def admi (request):
    username=None
    form_login=FormLogin()
    if request.method=='POST':
        form_login=FormLogin(request.POST)
        if form_login.is_valid():
            username=form_login.cleaned_data['username']
            password=form_login.cleaned_data['password']
            if username.strip() =='Project' and password.strip()=="python2020":
                request.session['username']=username
            else:
                username=None
   
    return render(request,'lists/admi.html',{'demo title':'session','form_login':form_login,'username':username})    
   