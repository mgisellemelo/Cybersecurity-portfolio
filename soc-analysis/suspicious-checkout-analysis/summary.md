🔎 1. Observamos tráfico HTTP en una app (probablemente vulnerable)
Objetivo: detectar fugas de información o acciones inseguras a través de tráfico interceptado.

Herramientas: Proxy (como Burpsuite y Wireshark, navegador web.

🧠 2. Detectamos tráfico de un pedido/orden
Ejemplo observado:

json
{
  "orderId": "5267-9f367f132911792b",
  "email": "*dm*n@j**c*-sh.*p",
  "products": [...],
  "totalPrice": 24.92,
  "delivered": false
}

Interpretación:
La API /rest/admin/orders devuelve pedidos aunque el usuario es un administrador.

Podemos ver:

Email (aunque parcialmente ofuscado).

Productos comprados.

Detalles de entrega.

Riesgo: Fuga de información sensible a través de endpoint de admin sin control de acceso adicional.


💳 3. Vimos detalles de la tarjeta de pago

json
{
  "cardNum": "************4368",
  "expMonth": 2,
  "expYear": 2081
}


Interpretación:
El backend devuelve parte del número de tarjeta del usuario Administrator.

Si bien el número está parcialmente ofuscado, no debería devolverse nunca al cliente.

Riesgo: Fuga parcial de datos de tarjeta (PCI-DSS violación potencial).


📦 4. Checkout realizado por el admin

http
POST /rest/basket/1/checkout

Payload utilizado:

json
{
  "orderDetails": {
    "paymentId": "3",
    "addressId": "3",
    "deliveryMethodId": "1"
  }
}


Interpretación:
Usamos el token del admin para hacer checkout de su propio carrito.

Es posible modificar basketId en la URL y posiblemente realizar pedidos en nombre de otros usuarios.

Riesgo: Acción crítica sin verificación de propiedad del recurso → Broken Access Control (IDOR).

