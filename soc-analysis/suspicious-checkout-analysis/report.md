# 🕵️‍♀️ Security Findings Report – Broken Access Control (Juice Shop)



## 📌 Contexto
Durante un análisis de tráfico en una instancia de OWASP Juice Shop, se identificaron vulnerabilidades críticas relacionadas con **Broken Access Control (BAC)**, **exposición de datos sensibles** y **falta de control de roles**. Este informe detalla los hallazgos, cómo fueron detectados y cómo podrían ser mitigados.

## 🔍 Hallazgos

### 1. 🔓 Insecure Direct Object Reference (IDOR)
- **Descripción:** La aplicación permite el acceso directo a recursos mediante IDs predecibles (por ejemplo: `/rest/basket/1/checkout`).
- **Impacto:** Un usuario autenticado (o administrador) puede realizar acciones sobre objetos que no le pertenecen.
- **Evidencia técnica:**
  ```http
  POST /rest/basket/1/checkout
  Authorization: Bearer <admin_token>


**Riesgo: Alto**

**Recomendación:**

-Validar la propiedad de los objetos antes de permitir acciones.

-Usar UUIDs o referencias seguras en lugar de IDs secuenciales.


###2. 💳 Exposición de Datos Sensibles (PII/PCI Violation)
Descripción: La API devuelve información sensible parcialmente enmascarada.
 json
{
  "cardNum": "************4368",
  "expMonth": 2,
  "expYear": 2081
}

Impacto: Violación de normativas como PCI DSS.

**Riesgo: Medio-Alto**

**Recomendación:**

-Evitar retornar cualquier dato sensible innecesario.

-Implementar controles estrictos de logging y auditoría sobre endpoints sensibles.

 
 
###3. 🛡️ Falta de control de privilegios (Role Bypass)
Descripción: Un usuario con rol admin puede ver información asociada a otros usuarios sin restricciones.

json
{
  "email": "*dm*n@j**c*-sh.*p"
}

**Riesgo: Medio**

**Recomendación:**

-Implementar controles de acceso basados en roles (RBAC) con validaciones por recurso.

-Evitar exponer información de usuarios sin consentimiento explícito o necesidad funcional.



### 4. Acceso no autorizado a información sensible de envíos

Ruta afectada: GET /api/Deliverys/1

Tipo: Exposición de información sensible

Autenticación: Bypass con JWT de administrador obtenido mediante SQL Injection

-Impacto:
**Riesgo: medio-alto**

Acceso a detalles de métodos de entrega

Posible modificación si la API permite métodos PUT

⚖️ Cumplimientos que esto podría violar:
      -PCI DSS 3.2.1 → Nunca almacenar ni devolver PAN completo sin justificación.

      -OWASP Top 10 - A01:2021 Broken Access Control

      -A04:2021 Insecure Design / Sensitive Data Exposure (antigua A03)

 **Recomendación:**

-Implementar controles de acceso basados en roles (RBAC) con validaciones por recurso.

-Evitar exponer información de usuarios sin consentimiento explícito o necesidad funcional.



##
📈 Análisis desde perspectiva SOC
Indicadores de actividad sospechosa:

Múltiples intentos sobre IDs de objetos secuenciales.

Accesos fuera del horario habitual o desde IPs distintas.

Recomendaciones para detección:

Activar alertas en SIEM ante accesos a recursos de otros usuarios.

Revisar logs de acceso a endpoints /rest/basket/*, /rest/order/*, etc.



##🛡️ 5. Recomendaciones


Categoría | Recomendación
Access Control | Validar propiedad de recursos en el backend.
Logging & Monitoring | Activar alertas por acceso anómalo a recursos críticos.
Data Minimization | No devolver ningún dato PII/PCI si no es estrictamente necesario.
API Hardening | Usar scopes, roles y claims dentro del JWT y validarlos en cada endpoint.
Secure Development | Implementar pruebas automatizadas para detectar IDOR y exposición de datos.

(Validación de roles en cada endpoint, Revocación o expiración de tokens comprometidos, Monitoreo de actividades anómalas con privilegios de admin, Restringir acceso incluso entre roles privilegiados, Evitar que el cliente controle acciones críticas como ver pedidos de otros usuarios).

##
🛠️ Mitigaciones y buenas prácticas

Componente	Recomendación
API Access Control	Validar siempre ownership del recurso desde el backend.
JWT Handling	Revisar role, userId y claims antes de ejecutar acciones.
Logging	Registrar todas las acciones administrativas e inusuales.
Testing	Incluir pruebas automáticas de IDOR, RBAC y fuga de datos en el CI/CD.

