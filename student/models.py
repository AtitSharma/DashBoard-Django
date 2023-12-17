from django.db import models
from utils.models import User, TimeStampAbstractModel
from semester.models import Semester


class StudentProfile(TimeStampAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_user")
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING,related_name="student_semester")
