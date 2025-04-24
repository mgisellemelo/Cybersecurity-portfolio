💥 Feedback Injection sin autenticación
##
**🔍 Durante el análisis de la aplicación vulnerable**, se identificó que el endpoint:

bash

POST /api/Feedbacks/

permite enviar comentarios sin autenticación y con validación mínima del contenido.
🧪 Payload usado:
json

{
  "captchaId": 1,
  "captcha": "160",
  "comment": "really bad bad bad (anonymous)",
  "rating": "1"
}

📬 Respuesta del servidor:
Código HTTP: 201 Created


Feedback almacenado con "UserId": null


Sin verificación de sesión ni autorización.

##
**🔍 Hallazgos:**
Permite spam y posible abuso masivo del endpoint.


Si se combinara con XSS (<script> en comentarios), podría explotarse.


captchaId y captcha pueden ser manipulados para bypass (validación débil).

##
**🛡️ Recomendaciones:**
Requiere autenticación para enviar feedback (o aplicar mecanismos de limitación).


Validación fuerte del captcha y contenido.


Sanitización del campo comment.

