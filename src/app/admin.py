from django.contrib import admin
from .models import Categoria, Producto, Ingrediente, ProductoIngrediente, Cliente, Pedido, DetallePedido

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(ProductoIngrediente)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
