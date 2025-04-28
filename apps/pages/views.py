from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from django.contrib.auth.decorators import login_required
from .forms import PageForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.db.models import Q


# Create your views here.

# Listar todas las páginas
def pages_list(request):
    pages = Page.objects.all()
    return render(request, 'pages/pages_list.html', {'pages': pages})

# Ver detalle de una página
def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})

# Crear una nueva página (solo logueados)
@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)  # NO guardamos todavía
            page.user = request.user        # Asociamos el usuario logueado
            page.save()                     # Ahora sí guardamos
            messages.success(request, "Página creada exitosamente.")
            return redirect('pages_list')
    else:
        form = PageForm()
    return render(request, 'pages/page_form.html', {'form': form, 'titulo': 'Crear Nueva Página'})

# Editar una página (solo logueados)
@login_required
def page_update(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    
    if page.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para editar esta página.")

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('pages_list')
    else:
        form = PageForm(instance=page)
    
    return render(request, 'pages/page_form.html', {'form': form})

# Eliminar una página (solo logueados)
@login_required
def page_delete(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if page.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para eliminar esta página.")

    if request.method == 'POST':
        page.delete()
        return redirect('pages_list')
    
    return render(request, 'pages/page_confirm_delete.html', {'page': page})

def buscar_page(request):
    query = request.GET.get('q')
    resultados = Page.objects.filter(
        Q(title__icontains=query) | Q(subtitle__icontains=query) | Q(content__icontains=query)
    ) if query else None

    return render(request, 'pages/buscar_page.html', {'resultados': resultados, 'query': query})