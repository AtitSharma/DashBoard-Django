from django.shortcuts import render
from django.views import View
from student.models import StudentProfile
from utils.models import User


class StudentDashBoardView(View):
    def get(self,request, *args, **kwargs):
        student_content = StudentProfile.objects.all()
        student_user = User.objects.filter(is_student=True)
        return render(request, "student_dashboard.html", {"student_content": student_content, "student_user": student_user})


