from django.shortcuts import render, get_object_or_404

from .models import Producto, Cliente, Pedido
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm
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

from django.contrib.auth.models import User
from django.db.utils import IntegrityError

#user = User.objects.create_user('Madelaiane', 'madelaine@dominio.com', '123456789')
#user.first_name = 'Madelaine'
#user.last_name = 'Colicheo'
#user.save()


@login_required
def protected_view(request):
    # Vista protegida solo para usuarios autenticados.
    return render(request, 'app/protected_page.html')


def index(request):
    return render(request, 'app/index.html')

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
                  
def login(request):
    #user = User.objects.create_user('Madelaiane', 'madelaine@dominio.com', '123456789')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Has iniciado sesión exitosamente!")
                return redirect('app:index')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Formulario inválido.")
    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})

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


def logout(request):
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('app:index')


def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:productos')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})
