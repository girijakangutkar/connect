from django import forms
from .models import job,Applicants 
from django.contrib.auth.models import User



# Create your forms here.
class ApplyForm(forms.ModelForm):

    class Meta:
        model = Applicants
        fields = ('Name', 'ssc','Hsc','Postgrad_cgpa','Resume')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
  
    class Meta:
        model = User 
        fields = ('username','email','password')

    
