from django import forms
from utils.models import User
from utils.model_status import Gender

class UserRegistrationForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=255,min_length=8,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255,min_length=8,widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255,required=False)
    date_of_birth=  forms.DateField()
    mobile_number = forms.IntegerField()
    gender = forms.ChoiceField(choices=Gender)
    address = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The provided email aready exits in our system")
        return email
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1!=password2:
            raise forms.ValidationError("The provided password did'nt match with each other ")
        return self.cleaned_data
    

    def save(self,commit=True):
        email = self.cleaned_data.get("email")
        password=self.cleaned_data.get("password2")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        middle_name = self.cleaned_data.get("middle_name")
        date_of_birth = self.cleaned_data.get("date_of_birth")
        gender = self.cleaned_data.get("gender")
        mobile_number = self.cleaned_data.get("mobile_number")
        address = self.cleaned_data.get("address") 
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,middle_name=middle_name,mobile_number=mobile_number,
                    date_of_birth=date_of_birth,gender=gender,address=address)
        user.set_password(password)
        if commit:
            user.save()
        return user
    

class LoginUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
