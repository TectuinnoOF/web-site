from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'email',
            'ocupacion',
            'area_interes',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Tu apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Tu correo'}),
        }
