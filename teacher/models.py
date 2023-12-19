from django.db import models
from utils.models import User, TimeStampAbstractModel


class TeacherProfile(TimeStampAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_user")
    degree = models.CharField(max_length=100, blank=True, null=True)
    