from django.contrib import admin
from .models import Autor, Categoria, Post

admin.site.register(Autor)
admin.site.register(Categoria)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha')  # columnas que se ven
    list_filter = ('autor', 'categoria', 'fecha')  # filtros en la barra lateral
    search_fields = ('titulo', 'contenido')  # barra de búsqueda arriba
    date_hierarchy = 'fecha'  # filtro por fechas con navegación
