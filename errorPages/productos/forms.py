from django import forms
from .models import Producto

#Podemos crear un formulario para modelo que exista
class productoForm(forms.ModelForm):
    #La clase Meta (Metainfo del formulario)
    class Meta:
        #Definir a que modelo se basa el formulario
        model = Producto
        
        #Definir que campos van a ser incluido en el formulario
        fields = ['nombre', 'precio', 'imagen']

        #Definir como se deben de ver o que atributos tiene los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio',
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen del producto',
                }
            ),
        }

        #Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre':{
                'required':'El nombre es obligatorio'
            },
            'precio':{
                'required':'El precio no puede estar vacio', 'invalid': 'Ingrese un numero valido'
            },
        }