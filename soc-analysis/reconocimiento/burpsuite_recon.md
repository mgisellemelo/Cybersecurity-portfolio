# 🔍 Análisis con BurpSuite - OWASP Juice Shop

## 🧠 Objetivo

Interceptar tráfico entre el navegador y Juice Shop para identificar vulnerabilidades web comunes.

---

## 🛠️ Herramientas

- Kali Linux
- BurpSuite Community Edition
- Firefox (para configurar proxy)
- OWASP Juice Shop (`http://localhost:3000`)

---

## 🧪 Paso a paso

### 1. Iniciar Juice Shop

Opcion 1: DOCKER
docker run -d -p 3000:3000 bkimminich/juice-shop

Opcion 2: NODE
Download el repositorio de Juice-shop desde Github hasta tu maquina local.
Situate en la carpeta y corre los comandos mpn run y mpn start.
Luego abri tu navegador y coloca tu IP+:3000

![Skärmbild 2025-04-16 174038](https://github.com/user-attachments/assets/958232bd-3b9c-4bd4-9fd3-ca9bb96d1948)

### 2. Iniciar BurpSuite

Desde tu terminal en KaliLinux coloca el comando:
sudo burpsuite

Esto va a abrir el programa en donde vas a iniciar un proyecto nuevo.
![Skärmbild 2025-04-16 174032](https://github.com/user-attachments/assets/762c045d-7d17-4008-a4a6-54ea7cabcdf1)


### 3. Configura tu proxy


Podes hacerlo con Foxy Proxy o manualmente desde el navegador
Lo importante es que uses el dominio 127.0.0.1 y el puerto 8080 que es el que usa Burpsuite.
![Skärmbild 2025-04-16 181436](https://github.com/user-attachments/assets/69791a2c-3b05-42d4-b0f9-08fb09ed463d)



### 4. Usando Burpsuite
Ahora nos situamos en Burpsuite y le damos turn on en la ventana de proxy. Este programa va a interceptar el trafico y nos va a ayudar a hacer un reconocimiento de la pagina web.
Tambien nos permite modificar las peticiones.

Por ejemplo:
### 
Podemos modificar un comentario de la pagina interceptando la peticion put y cambiando el contenido del mismo.
###
Tambien podemos hacer una injeccion sql para podemos iniciar sesion interceptando la peticion de un usuario que acaba de iniciar sesion como lo muestra la imagen de abajo. Se modifico el usuario por " ' OR 1=1 ". Esto nos da acceso a la web como usuario admin.


![Skärmbild 2025-04-16 173044](https://github.com/user-attachments/assets/19c58e5c-cb9b-4a89-9b2b-a5091e610f90)


