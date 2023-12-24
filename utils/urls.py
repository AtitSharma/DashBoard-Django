from django.urls import path
from utils.views import RegisterStudentAccountView,LoginUser


app_name = "utils"
urlpatterns = [
    path("student-register/",RegisterStudentAccountView.as_view(),name="register-student"),
    path("user-login/",LoginUser.as_view(),name="login-user")
]
