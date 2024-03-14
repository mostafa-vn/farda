from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    phone = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'تلفن همراه'}))
    email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'ایمیل'}))
    city = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'شهر سکونت'}))
    birth_date = forms.DateField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'تاریخ تولد'}))
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'email', 'city', 'birth_date']

class SkillsForm(forms.ModelForm):
    python = forms.IntegerField(required=False, label='پایتون', widget=forms.TextInput(attrs={'type':'number', 'min':'0', 'max':'10'}))
    bash = forms.IntegerField(required=False, label='بش')
    linux = forms.IntegerField(required=False, label='لینوکس')

    class Meta:
        model = Profile
        fields = ['python', 'bash', 'linux']


class NetworksForm(forms.ModelForm):
    network1 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network2 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network3 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network4 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network5 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network6 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network7 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network8 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network9 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))
    network10 = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'توضیحات'}))

    class Meta:
        model = Profile
        fields = ['network1']