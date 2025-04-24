 Hallazgo: Acceso no autorizado a información sensible de envíos
Ruta afectada: GET /api/Deliverys/1

Tipo: Exposición de información sensible

Autenticación: Bypass con JWT de administrador obtenido mediante SQL Injection

Impacto:

Acceso a detalles de métodos de entrega

Posible modificación si la API permite métodos PUT

Recomendaciones:

Validación de roles en cada endpoint

Revocación o expiración de tokens comprometidos

Monitoreo de actividades anómalas con privilegios de admin
