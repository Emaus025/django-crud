from django import forms
from .models import Partitura

class PartituraForm(forms.ModelForm):
    class Meta:
        model = Partitura
        fields = [
            'titulo',
            'compositor',
            'arreglista',
            'genero',
            'instrumentos',
            'dificultad',
            'archivo',
            'descripcion',
            'visibilidad',
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la partitura'}),
            'compositor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del compositor'}),
            'arreglista': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del arreglista'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Género musical'}),
            'instrumentos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instrumentos'}),
            'dificultad': forms.Select(attrs={'class': 'form-control'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la partitura'}),
            'visibilidad': forms.Select(attrs={'class': 'form-control'}),
        }