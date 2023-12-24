from django.shortcuts import render
from django.views import View
from utils.forms import StudentRegisterForm
# Create your views here.



class RegisterStudentAccountView(View):
    def post(self,request,*args,**kwargs):
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # return redirect()
        return render(request,"student_register.html",context={"form":form})
        
    def get(self,request,*args,**kwargs):
        form = StudentRegisterForm()
        context = {
            "form":form
        }
        # return render(request,"student_register.html",context=context)