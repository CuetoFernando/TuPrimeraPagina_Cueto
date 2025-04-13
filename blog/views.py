from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post, Autor, Categoria



# ------------------------BASE-----------------------------------------------------
def inicio(request):
    return render(request, 'blog/base.html')

def mi_blog(request):
    descripcion = "Bienvenido a Mi Blog. Este espacio está dedicado a compartir publicaciones familiares, pensamientos y aprendizajes compartidos. ¡Explorá, aprendé y compartí!"
    return render(request, 'blog/mi_blog.html', {'descripcion': descripcion})


# ------------------------AUTOR POST-----------------------------------------------
def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            
            if Autor.objects.filter(nombre=nombre, apellido=apellido, email=email).exists():
                messages.error(request, "Este autor ya está registrado.")
            else:
                form.save()
                messages.success(request, "Autor guardado correctamente.")
    else:
        form = AutorForm()
    
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Autor'})


# ------------------------CATEGORIA POST-----------------------------------------------
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            
            if Categoria.objects.filter(nombre=nombre, descripcion=descripcion).exists():
                messages.error(request, "La categoría ya existe.")
            else:
                form.save()
                messages.success(request, "Categoría creada con éxito.")
    else:
        form = CategoriaForm()
    
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

# ------------------------CREAR POST-----------------------------------------------
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post creado con éxito.")
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

# ------------------------ACCESO POST-----------------------------------------------
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})