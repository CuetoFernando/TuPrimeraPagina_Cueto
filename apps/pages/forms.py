from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title','subtitle', 'content', 'image']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la página'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subtítulo opcional'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
