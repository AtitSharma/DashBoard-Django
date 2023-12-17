from django.db import models
from utils.models import TimeStampAbstractModel


class Subject(TimeStampAbstractModel):
    name = models.CharField(max_length=200)
