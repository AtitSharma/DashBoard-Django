from django.urls import path
from teacher.views import TeacherDashboardView


app_name = "teacher"

urlpatterns = [
    path("teacher-dashboard/", TeacherDashboardView.as_view(), name="teacher-dashboard"),
]
