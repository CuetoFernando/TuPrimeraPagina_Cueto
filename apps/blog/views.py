from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post, Autor, Categoria
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required

def post_list(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/post_list.html', {'posts': posts})

# ------------------------BASE-----------------------------------------------------
def inicio(request):
    return render(request, 'blog/base.html')

def mi_blog(request):
    descripcion = "Bienvenido a Mi Blog. Este espacio está dedicado a compartir publicaciones familiares, pensamientos y aprendizajes compartidos. ¡Explorá, aprendé y compartí!"
    return render(request, 'blog/mi_blog.html', {'descripcion': descripcion})


# ------------------------COMO FUNCIONA (USUARIO LOGUEADO)-------------------------

def como_funciona(request):
    return render(request, 'blog/como_funciona.html')


# ------------------------AUTOR POST-----------------------------------------------
def admin_required(login_url='login'):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)

@staff_member_required
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
@admin_required()
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
@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            # Buscar si ya existe Autor por el user
            autor = Autor.objects.filter(user=request.user).first()

            # Si NO existe, buscamos por email
            if not autor:
                autor = Autor.objects.filter(email=request.user.email).first()

            # Si no existe ni por user ni por email, lo creamos
            if not autor:
                autor = Autor.objects.create(
                    user=request.user,
                    nombre=request.user.first_name or request.user.username,
                    apellido=request.user.last_name or '',
                    email=request.user.email
                )

            post.autor = autor
            post.save()
            messages.success(request, "Post creado con éxito.")
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Crear Post'})


# ------------------------BUSCAR POST-----------------------------------------------
def buscar_post(request):
    resultados = []
    if request.GET:
        formulario = BuscarPostForm(request.GET)
        if formulario.is_valid():
            titulo = formulario.cleaned_data.get('titulo')
            autor = formulario.cleaned_data.get('autor')
            categoria = formulario.cleaned_data.get('categoria')

            resultados = Post.objects.all()

            if titulo:
                resultados = resultados.filter(titulo__icontains=titulo)
            if autor:
                resultados = resultados.filter(autor__nombre__icontains=autor) | resultados.filter(autor__apellido__icontains=autor)
            if categoria:
                resultados = resultados.filter(categoria__nombre__icontains=categoria)

    else:
        formulario = BuscarPostForm()
    
    return render(request, 'blog/buscar.html', {'form': formulario, 'resultados': resultados})

# ------------------------ACCESO POST-----------------------------------------------
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#-------------------------EDITAR Y BORRAR POST (ADMIN)----------------------------

def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

@admin_required
def editar_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post actualizado exitosamente.")
            return redirect('buscar_post')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Editar Post'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})

