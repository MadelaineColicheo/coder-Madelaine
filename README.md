# Coder-MadelaineColicheo
# Curso Python

## Comisión

Comisión: 60095

Profesor: Esteban Acevedo

## Alumno

Nombre: Madelaine Colicheo

## Entrega
Modelo de Base de Datos para una Fábrica de Masas y Empanadas

1. Tabla: Productos
Esta tabla almacenará información sobre cada producto que fabrica la empresa (masas, empanadas, etc.).

Campo	Tipo de Dato	Descripción
id_producto	INT (PK, AUTO_INCREMENT)	Identificador único del producto
nombre	VARCHAR(100)	Nombre del producto (Ej. Empanada de pino, Masa para pizza)
descripcion	TEXT	Descripción breve del producto
categoria_id	INT (FK)	Relación con la categoría (Ej. empanadas, masas)
precio	DECIMAL(10,2)	Precio del producto
imagen	VARCHAR(255)	Ruta o URL de la imagen del producto
disponibilidad	BOOLEAN	Indica si el producto está disponible para la venta

2. Tabla: Categorías
Almacena las categorías de los productos (Ej. Empanadas, Masas, Comidas).

Campo	Tipo de Dato	Descripción
id_categoria	INT (PK, AUTO_INCREMENT)	Identificador único de la categoría
nombre	VARCHAR(100)	Nombre de la categoría (Ej. Empanadas, Masas)
descripcion	TEXT	Descripción de la categoría

3. Tabla: Ingredientes
Si necesitas información sobre los ingredientes de cada producto (por ejemplo, para mostrar alergias, valores nutricionales, etc.).

Campo	Tipo de Dato	Descripción
id_ingrediente	INT (PK, AUTO_INCREMENT)	Identificador único del ingrediente
nombre	VARCHAR(100)	Nombre del ingrediente (Ej. carne de res, cebolla)
descripcion	TEXT	Descripción del ingrediente

4. Tabla: Producto_Ingredientes
Una tabla de relación entre productos e ingredientes, ya que un producto puede tener varios ingredientes y un ingrediente puede estar presente en varios productos.

Campo	Tipo de Dato	Descripción
id_producto	INT (FK)	Relación con la tabla de productos
id_ingrediente	INT (FK)	Relación con la tabla de ingredientes

5. Tabla: Clientes
Si la página también tiene un sistema de clientes (por ejemplo, para pedidos online o para mantener un registro de clientes frecuentes).

Campo	Tipo de Dato	Descripción
id_cliente	INT (PK, AUTO_INCREMENT)	Identificador único del cliente
nombre	VARCHAR(100)	Nombre del cliente
email	VARCHAR(150)	Correo electrónico del cliente
telefono	VARCHAR(15)	Teléfono del cliente
direccion	VARCHAR(255)	Dirección del cliente

6. Tabla: Pedidos
Si quieres ofrecer una opción de compra online o registrar pedidos hechos a la fábrica.

Campo	Tipo de Dato	Descripción
id_pedido	INT (PK, AUTO_INCREMENT)	Identificador único del pedido
id_cliente	INT (FK)	Relación con la tabla de clientes
fecha	DATETIME	Fecha y hora del pedido
total	DECIMAL(10,2)	Total del pedido
estado	VARCHAR(50)	Estado del pedido (pendiente, enviado, entregado)

7. Tabla: Detalle_Pedido
Esta tabla almacena los productos solicitados en cada pedido (uno a muchos entre pedido y productos).

Campo	Tipo de Dato	Descripción
id_detalle	INT (PK, AUTO_INCREMENT)	Identificador único del detalle
id_pedido	INT (FK)	Relación con la tabla de pedidos
id_producto	INT (FK)	Relación con la tabla de productos
cantidad	INT	Cantidad del producto en el pedido
precio_unitario	DECIMAL(10,2)	Precio del producto en ese pedido
