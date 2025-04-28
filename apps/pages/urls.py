from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages_list, name='pages_list'),
    path('crear/', views.page_create, name='page_create'),
    path('<int:page_id>/editar/', views.page_update, name='page_update'),
    path('<int:page_id>/eliminar/', views.page_delete, name='page_delete'),
     path('<int:pk>/', views.page_detail, name='page_detail'),
     path('buscar/', views.buscar_page, name='buscar_page'),
]
