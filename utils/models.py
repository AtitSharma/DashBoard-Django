from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,AbstractUser
from utils.model_status import Gender
from django.db.models import Q
import datetime



class CustomUserManager(BaseUserManager):
    '''
        Custom Manager to Create User and SuperUser
    '''
    def create_user(self,email,password=None,**extra_fields):
        '''
            Create Normal Users
        '''
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        '''
            Create Super User
        '''
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        '''
            Super must have all properties of normal user
        '''
        return self.create_user(email,password,**extra_fields)
        






class User(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    username=None
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20,choices=Gender.choices)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50)  
    name =  models.CharField(max_length=255)  
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def save(self,*args,**kwargs):
        if(len(self.first_name)>0 and len(self.middle_name)>0 and len(self.last_name)>0):
            self.name = self.first_name + " " + self.middle_name + " " + self.last_name
        elif(len(self.first_name)>0 and len(self.last_name)>0):
            self.name = self.first_name + " " + self.last_name
        super(User,self).save(*args,**kwargs)


    objects=CustomUserManager()
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        constraints = [
            models.CheckConstraint(
                check=Q(is_student=True, is_teacher=False) | Q(is_student=False, is_teacher=True),
                name='unique_identity'
            )
        ]
        

    
    
class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    

class Attendance(TimeStampAbstractModel):
    from_time = models.TimeField()
    to_time = models.TimeField()
    duration = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_attendance")
    
    def save(self, *args, **kwargs):
        if self.from_time and self.to_time:
            time_difference = datetime.datetime.combine(datetime.date.today(), self.to_time) - datetime.datetime.combine(datetime.date.today(), self.from_time)
            time_difference_seconds = time_difference.total_seconds()
            self.duration = datetime.timedelta(seconds=time_difference_seconds)

        super(Attendance, self).save(*args, **kwargs)
    

