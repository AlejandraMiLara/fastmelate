
from django import forms
from .models import NumeroSorteo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NumeroSorteoForm(forms.ModelForm):
    class Meta:
        model = NumeroSorteo
        fields = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6']

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        help_text=None  
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput,
        help_text=None  
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None 
