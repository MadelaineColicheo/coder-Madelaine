from django.shortcuts import render, get_object_or_404

from .models import Producto, Cliente, Pedido, Categoria

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductoForm
from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ProductoForm, CategoriaForm  # Asegúrate de importar ambos formularios


def index(request):
    return render(request, 'app/index.html', {'user': request.user})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/productos.html', {'productos': productos})

def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'app/producto_detalle.html', {'producto': producto})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app/clientes.html', {'clientes': clientes})

def pedido_detalle(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    return render(request, 'app/pedido_detalle.html', {'pedido': pedido})

def profile(request):
    return render(request, 'app/profile.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')
                  
'''def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app:index')  # O la URL a la que quieras redirigir después de iniciar sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
'''                
class login(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'app/login.html'
    next_page = reverse_lazy('app:index')

    def form_valid(self, form: AuthenticationForm) -> HttpResponse:
        usuario = form.get_user()
        messages.success(
            self.request, f'Inicio de sesión exitoso ¡Bienvenido {usuario.username}!'
        )
        return super().form_valid(form)
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "¡Cuenta creada exitosamente!")
                return redirect('app:login')  # Redirigir al login después de crear la cuenta
            except IntegrityError:
                messages.error(request, "El nombre de usuario ya está en uso.")
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/register.html', {'form': form})

#@login_required
#def logout(request):
 #   messages.success(request, "Has cerrado sesión exitosamente.")
 #     return redirect('app:index')
@login_required
def listar_productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'app/listar_productos.html', {'productos': productos})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('app:listar_productos')  # Vuelve a la lista de productos
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all()  # Obtiene todas las categorías
    return render(request, 'app/listar_categorias.html', {'categorias': categorias})

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app:listar_categorias')  # Vuelve a la lista de categorías
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'app/editar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return HttpResponseRedirect(reverse('app:listar_productos'))

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return HttpResponseRedirect(reverse('app:listar_categorias'))

