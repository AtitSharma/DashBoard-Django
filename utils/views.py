from django.shortcuts import render,redirect
from django.views import View
from utils.forms import StudentRegisterForm,LoginUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.



class RegisterStudentAccountView(View):
    def post(self,request,*args,**kwargs):
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # return redirect()
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
                if user.is_student :
                    # return redirect()
                    pass
                if user.is_teacher:
                       # return redirect()
                    pass
        return render(request,"user_login.html")    
        

