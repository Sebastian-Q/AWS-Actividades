import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
    
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo electrónico',
                    'required': True,
                    'pattern': '^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Completo',
                    'required': True,
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos',
                    'required': True,
                }
            ),
            'control_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Número de control',
                    'required': True,
                    'pattern': '^\d{5}[a-zA-Z]{2}\d{3}$'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                    'required': True,
                }
            ),
            'tel': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Teléfono',
                    'required': True,
                    'maxlength': 10,
                    'minlength': 10
                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': True,
                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Confirmar Contraseña',
                    'required': True,
                }
            ),
            
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r'^[0-9]{5}tn[0-9]{3}@utez\.edu\.mx$'
        if not re.match(pattern, email):
            raise forms.ValidationError("El correo electrónico debe pertenecer al dominio @utez.edu.mx y cumplir con el formato correcto.")
        return email

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^\d{5}[a-zA-Z]{2}\d{3}$', control_number):
            raise forms.ValidationError("El número de control debe contener 10 caracteres en el formato correcto.")
        return control_number
    
    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError("El número de teléfono debe contener exactamente 10 dígitos.")
        return tel
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[!#$%&?]', password1):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo (!, #, $, %, & o ?).")
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class CustomUserLoginForm(AuthenticationForm):
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password) # type: ignore
            if not user:
                raise forms.ValidationError("Usuario o contraseña incorrectos.")
        return cleaned_data
    
    pass