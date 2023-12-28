from django.shortcuts import render
from django.views import View


class TeacherDashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "teacher_dashboard.html")
