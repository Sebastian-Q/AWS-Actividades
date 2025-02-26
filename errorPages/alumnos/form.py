from django import forms
from .models import Alumno

#Podemos crear un formulario para modelo que exista
class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']

        #Definir como se deben de ver o que atributos tiene los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Alumno',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellidos del Alumno',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Edad',
                }
            ),
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Matricula',
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo Electronico', 
                }
            ),
        }

        #Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre del Alumno',
            'apellido': 'Apellidos del Alumno',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo Electronico',
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre':{
                'required':'El nombre es obligatorio'
            },
            'apellido':{
                'required':'El apellido es obligatorio'
            },
            'edad':{
                'required':'La edad no puede estar vacia', 'invalid': 'Ingrese una edad valida'
            },
            'matricula':{
                'required':'La matricula es obligatoria', 'unique': 'La matricula ya existe'
            },
            'correo':{
                'required':'El correo es obligatorio', 'invalid': 'Ingrese un correo valido', 'unique': 'El correo ya existe'
            },
        }