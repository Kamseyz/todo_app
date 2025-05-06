from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


# REGISTRATION FORM
class Registration(UserCreationForm):
    email = forms.EmailField(help_text='Pls enter your email address')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    # SAVE FORM
    
    def save(self, commit = True):
        user  = super().save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    
    #CHECK IF EMAIL ALREADY EXIST
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise ValidationError('Email already exist')
        return email


# LOGIN FORM
class Login(forms.Form):
    email = forms.EmailField(required= True)
    password = forms.CharField(widget= forms.PasswordInput)