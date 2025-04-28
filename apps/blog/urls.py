from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('mi_blog/', views.mi_blog, name='mi_blog'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('editar_post/<int:post_id>/', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:pk>/', views.eliminar_post, name='eliminar_post'),
]


