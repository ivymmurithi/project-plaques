from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_picture','bio','contact_info']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['website_picture','title','description','website_link']

class VotingForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['design_score','usability_score','content_score']
        widgets = {
            'Dropdown': forms.Select(attrs={'id':'choice'}),
        }