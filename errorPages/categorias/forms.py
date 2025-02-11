from django import forms
from .models import Categoria

#Podemos crear un formulario para modelo que exista
class categoriaForm(forms.ModelForm):
    #La clase Meta (Metainfo del formulario)
    class Meta:
        #Definir a que modelo se basa el formulario
        model = Categoria
        
        #Definir que campos van a ser incluido en el formulario
        fields = ['nombre', 'imagen']

        #Definir como se deben de ver o que atributos tiene los campos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoria',
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen de la categoria',
                }
            ),
        }

        #Etiquetas personalizadas
        labels = {
            'nombre': 'Nombre de la categoria',
            'imagen': 'URL de la imagen'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre':{
                'required':'El nombre es obligatorio'
            },
        }