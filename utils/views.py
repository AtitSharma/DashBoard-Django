from django.shortcuts import render,redirect
from django.views import View
from utils.forms import UserRegistrationForm,LoginUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.



class UserRegistration(View):
    def post(self,request,*args,**kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("utils:login-user")
        return render(request,"user_register.html",context={"form":form})
        
    def get(self,request,*args,**kwargs):
        return render(request,"user_register.html")
        
        
class LoginUser(View):
    def get(self,request,*args,**kwargs):
        return render(request,"user_login.html")
    
    def post(self,request,*args,**kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.data.get("email")
            password = form.data.get("password")
            user = authenticate(email=email,password=password)
            if user:
                if user.is_student:
                    return redirect("student:student-dashboard")
                if user.is_teacher:
                    return redirect("teacher:teacher-dashboard")
                    pass
            # else:
            #     messages.add_message(request, messages.ERROR, "Invalid username and password")
            #     return redirect("utils:user-login")
        return render(request,"user_login.html")
    
    