from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

# ------------------------BASE-----------------------------------------------------
def inicio(request):
    return render(request, 'blog/base.html')


# ------------------------AUTOR POST-----------------------------------------------
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})


# ------------------------CATEGORIA POST-----------------------------------------------
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

# ------------------------CREAR POST-----------------------------------------------
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Post'})

# ------------------------BUSCAR POST-----------------------------------------------
def buscar_post(request):
    resultados = []
    if request.GET.get('titulo'):
        formulario = BuscarPostForm(request.GET)
        if formulario.is_valid():
            titulo = formulario.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        formulario = BuscarPostForm()
    return render(request, 'blog/buscar.html', {'form': formulario, 'resultados': resultados})

