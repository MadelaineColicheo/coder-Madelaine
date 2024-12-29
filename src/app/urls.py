# app/urls.py
from django.urls import path
from . import views
from .views import ProductoUpdateView


app_name = 'app'  # Nombre de la aplicación para referencias en las URLs / Deberia llamarse core

urlpatterns = [
    path('', views.index, name='index'),  # URL raíz que apunta a la vista 'index'
    path('profile/', views.profile, name='profile'),  # URL para la vista
    path('about/', views.about, name='about'),  # URL para la vista
    path('contact/', views.contact, name='contact'),  # URL para la vista
    path('login/', views.login, name='login'),  # URL para la vista
    path('register/', views.register, name='register'),  # URL para la vista
    path('logout/', views.logout, name='logout'),  # URL para la vista
    path('productos/', views.productos, name='productos'),  # URL para la vista de productos
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),  # URL para el detalle de un producto específico
    path('clientes/', views.clientes, name='clientes'),  # URL para la vista de clientes
    path('pedido/<int:id>/', views.pedido_detalle, name='pedido_detalle'),  # URL para el detalle de un pedido específico
]

urlpatterns += [
    path('producto/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_editar'),
]