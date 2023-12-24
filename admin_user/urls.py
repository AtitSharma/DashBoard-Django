from django.urls import path
from admin_user.views import AdminDashboardHomeView

app_name = "admin_user"

urlpatterns = [
    path("", AdminDashboardHomeView.as_view(), name="admin-home"),
]
