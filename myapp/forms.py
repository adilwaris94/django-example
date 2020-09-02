from django import forms
from myapp.models import User_pro,UserProfileInfo
from django.contrib.auth.models import User
class FormName(forms.Form):
        name=forms.CharField()
        emai=forms.EmailField()
        Text=forms.CharField(widget=forms.Textarea)

class SignupForm(forms.ModelForm):
    class Meta():
        model=User_pro
        fields='__all__'

class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
