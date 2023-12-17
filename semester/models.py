from django.db import models
from subject.models import Subject
from teacher.models import TeacherProfile
from utils.models import TimeStampAbstractModel



class Semester(TimeStampAbstractModel):
    subject = models.ManyToManyField(Subject, related_name="semester_subject")
    teacher = models.ManyToManyField(TeacherProfile, related_name="teacher_subject")
    
