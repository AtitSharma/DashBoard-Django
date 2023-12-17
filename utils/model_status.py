from django.db import models



class Gender(models.TextChoices):
    MALE = '1'
    FEMALE = '2'
    OTHERS = '3'