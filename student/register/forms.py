from django import forms
from.models import student



class Contact_Form(forms.Form):
    firstname=forms.CharField(max_length=20, label='Firstname Here',help_text="firstname",error_messages={'required': 'Please enter your firstname'})
    lastname=forms.CharField(max_length=20, label='secondname Here',help_text="username",error_messages={'required': 'Please enter your secondname'})
    username=forms.CharField(max_length=20, label='Username Here',help_text="username",error_messages={'required': 'Please enter your username'})
    password=forms.CharField(widget=forms.PasswordInput(),label='password Here',help_text="password",error_messages={'required': 'Please enter your password'})

class studentForm(forms.Form):
    username=forms.CharField(max_length=20, label='Username Here',help_text="username",error_messages={'required': 'Please enter your username'})
    password=forms.CharField(widget=forms.PasswordInput(),label='password Here',help_text="password",error_messages={'required': 'Please enter your password'})
