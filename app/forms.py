from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Employee

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={
        'class':'form-control',
        'name':'username',
        'id':'username',
        'maxlength':'15',
        'minlength':'5',
        'type':'text'
    }))
    email = forms.CharField(label='Email',widget=forms.TextInput(attrs={
        'class':'form-control',
        'name':'email',
        'id':'email',
        'type':'email',
        'placeholder':'example@gmail.com'
    }))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'name':'password1',
        'id':'password1',
        'maxlength':'16',
        'minlength':'5',
        'type':'password',
    }))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'name':'password1',
        'id':'password1',
        'maxlength':'16',
        'minlength':'5',
        'type':'password',
    }))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class EmployeeForm(ModelForm):
    emp_name = forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'Employee Name',
         'name':'emp_name',
         'id':'emp_name'
         })
    emp_email = forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'Employee Email',
         'name':'emp_email',
         'id':'emp_email'
         })
    emp_contact = forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'Employee Contact',
         'name':'emp_contact',
         'id':'emp_contact'
         })
    emp_salary = forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'Employee Salary',
         'name':'emp_salary',
         'id':'emp_salary'
         })

    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_email', 'emp_contact', 'emp_salary']
