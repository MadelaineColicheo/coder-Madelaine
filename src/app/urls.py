# app/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'app'  # Nombre de la aplicación para referencias en las URLs / Deberia llamarse core

urlpatterns = [
    path('', views.index, name='index'),  # URL raíz que apunta a la vista 'index'
    path('profile/', views.profile, name='profile'),  # URL para la vista
    path('about/', views.about, name='about'),  # URL para la vista
    path('contact/', views.contact, name='contact'),  # URL para la vista
    path('login/', views.login.as_view(), name='login'),  # URL para la vista
    path('register/', views.register, name='register'),  # URL para la vista
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),    
    path('productos-lista/', views.productos, name='productos-lista'),  # URL para la vista de productos
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),  # URL para el detalle de un producto específico
    path('clientes/', views.clientes, name='clientes'),  # URL para la vista de clientes
    path('pedido/<int:id>/', views.pedido_detalle, name='pedido_detalle'),  # URL para el detalle de un pedido específico
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),  # Vista para editar categoría
    path('productos/', views.listar_productos, name='listar_productos'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),  # Vista para editar producto
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]