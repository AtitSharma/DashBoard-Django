from django.urls import path
from utils.views import RegisterStudentAccountView


app_name = "utils"
urlpatterns = [
    path("student-register/",RegisterStudentAccountView.as_view(),name="register-student")
]
