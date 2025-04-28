from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'email']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        email = cleaned_data.get('email')

        if nombre and apellido and email:
            existe = Autor.objects.filter(
                nombre__iexact=nombre.strip(),
                apellido__iexact=apellido.strip(),
                email__iexact=email.strip()
            ).exists()

            if existe:
                raise forms.ValidationError("Ya existe un autor con estos datos.")
        
        return cleaned_data

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'categoria'] 

class BuscarPostForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=100, required=False)
    autor = forms.CharField(label='Autor', max_length=100, required=False)
    categoria = forms.CharField(label='Categoría', max_length=100, required=False)