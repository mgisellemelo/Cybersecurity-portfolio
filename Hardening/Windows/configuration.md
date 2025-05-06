🖥️ 1️⃣ Configuración de seguridad en Windows

###✅  1: Actualizar Windows y drivers###
Ve a Configuración > Actualización y seguridad > Windows Update

- Buscar actualizaciones

. Instala actualizaciones opcionales (drivers, firmware).

###✅ Paso 2: Configurar Windows Defender### 
Si tienes otro antivirus, Windows Defender no hace análisis activo, pero puedes configurarlo para análisis bajo demanda. También deja habilitada la opción de Análisis periódico.
 En Windows Defender activa protección en tiempo real, protección en la nube y contra alteraciones.

###✅ Paso 3: Configurar Firewall###
🔍 Si usas el firewall de Windows:

Ve a Firewall y protección de red

Confirma que está activo para red privada y pública

Pulsa Permitir una aplicación a través del firewall

Revisa qué aplicaciones tienen permisos → elimina apps que no uses

👉 Recomiendo desactivar acceso público para apps que solo uses en casa:

Busca Edge, Google Chrome, etc. y deja solo Privado activado

###✅ Paso 4: Activar BitLocker (si tienes Windows Pro)###
Ve a Panel de control > Cifrado de unidad BitLocker

Pulsa Activar BitLocker

Guarda tu clave de recuperación (en USB o cuenta Microsoft)

Elige cifrar todo el disco y modo compatible

###✅ Paso 5: Configurar UAC al máximo###
Escribe en el buscador: uac

Selecciona Cambiar configuración de Control de cuentas de usuario

Sube el control al nivel más alto (“Siempre notificar”)

###✅ Paso 6: Revisar servicios innecesarios###
Escribe services.msc en el buscador

Revisa servicios como:

Remote Desktop Services → deshabilitado si no usas RDP

Server → deshabilitado si no compartes carpetas

SSDP Discovery, UPnP Device Host → deshabilitados si no necesitas dispositivos UPnP




