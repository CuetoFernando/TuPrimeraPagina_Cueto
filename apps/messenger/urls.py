from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('enviar/', views.send_message, name='send_message'),
    path('mensaje/<int:pk>/', views.message_detail, name='message_detail'),
    path('eliminar/<int:pk>/', views.message_delete, name='message_delete'),
    path('enviados/', views.sent_messages, name='sent_messages'),
    path('enviados/<int:pk>/', views.sent_message_detail, name='sent_message_detail'),

]

