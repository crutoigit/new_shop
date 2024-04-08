from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
       
    # 1) inafara de parole caci ele trebuies redefinite
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'outline-none text-emerald-600 font-bold p-2'}),
        #     'email': forms.EmailInput(attrs={'class':'outline-none text-emerald-600 font-bold p-2'}),
        # }
    
    # 2) redefinerea fiecarui field
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username...',
        'class':'outline-none text-emerald-600 font-bold p-2'
        }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email...',
        'class':'outline-none text-emerald-600 font-bold p-2'
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password...',
        'class':'outline-none text-emerald-600 font-bold p-2'
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password...',
        'class':'outline-none text-emerald-600 font-bold p-2'
        }))
        

        
        

