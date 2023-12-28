from django.urls import path
from student.views import StudentDashBoardView


app_name = "student"

urlpatterns = [
    path("student-dashboard/", StudentDashBoardView.as_view(), name="student-dashboard"),
]
