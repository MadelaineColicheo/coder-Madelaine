from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Producto, Cliente, Pedido
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('app:login')

@method_decorator(login_required, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'disponibilidad', 'imagen']
    template_name = 'app/producto_form.html'
    success_url = reverse_lazy('app:productos')

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
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')

def logout(request):
    return render(request, 'app/logout.html')

from django.shortcuts import render, redirect
from .forms import ProductoForm

def producto_nuevo(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:productos')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})
