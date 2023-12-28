from django.urls import path
from utils.views import UserRegistration,LoginUser


app_name = "utils"
urlpatterns = [
    path("user-register/",UserRegistration.as_view(),name="register-user"),
    path("user-login/",LoginUser.as_view(),name="login-user")
]
