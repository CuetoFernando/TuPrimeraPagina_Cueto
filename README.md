# TuPrimeraPagina_Cueto
4ra PreEntrega CoderHouse_Python 

Esta es una aplicación web tipo blog creada en Django, que incluye funcionalidades de creación de Posts, Pages, autenticación de usuarios, perfiles personalizados, mensajería privada entre usuarios y control de permisos.
Permite la interacción entre usuarios registrados, y la administración total desde el panel de Django para superusuarios.

## Creación del Repositorio y Proyecto

1. Crear el repositorio en GitHub
2. Clonar el repositorio en local (git clone) con Windows PowerShell en la carpeta deseada 
3. Ingresamos en VSC en la carpeta donde alojamos el repositorio
4. Creamos el entorno virtual (python -m venv venv) 
5. Activamos el entorno virtual (.\venv\Scripts\activate)
6. instalamos Django (pip install django)
7. Creamos el proyecto (django-admin startproject TuPrimeraPagina_Cueto)
8. Creamos las app blog, account, messenger y pages (python manage.py startapp blog)
9. Configuramos settings.py, urls.py generales y de apps.
10. Se crean modelos (Autor, Categoría, Post, Page, Message, Profile).
11. Se crean formularios personalizados (forms.py)
12. Se Crean vistas basadas en funciones (FBV) y clases (CBV).
13. Se desarrollar templates y herencia desde base.html.
14. Incorporamos validaciones, permisos, autenticaciones, y control de sesiones.


## Funcionalidades

1. Home: Página de inicio personalizada según estado de login.
2. About: Información personal pública del creador de la web.
3. Pages: Listado, creación, búsqueda, edición y borrado de páginas (solo propios).
4. Crear posts de blog de una página web con autor y categoría (claves foráneas) 
4. Blog: Ver posts, buscar posts, crear posts (autogeneración de autor), editar y borrar posts (solo Admin).
5. Mensajes: Bandeja de entrada, mensajes enviados, enviar y responder mensajes.
6. Perfiles: Ver y editar datos del usuario, cambiar contraseña.
7. Autenticación: Registro, login y logout.
8. Administrador: Panel de Django mejorado con filtros por autor, categoría, fecha.

## Funcionalidades extra Agreagdos 
1. Autoasignación de autor al crear posts si no existe
2. Navbar dinámica: cambia según si el usuario está logueado o es admin.
3. Sistema de mensajería funcional entre usuarios.
4. Control de permisos: Solo el creador puede editar/borrar sus Pages. Solo admins pueden eliminar Posts.
5. Editor de texto enriquecido para Posts y Pages usando CKEditor.
6. Buscador avanzado en Pages y Posts (por título, categoría y autor).
7. Mensajes Flash en todas las operaciones (crear, editar, borrar).
8. Protección de archivos estáticos mediante .gitignore.

## Orden de prueba

1. Registrarse como nuevo usuario o ingresar como admin.
2. Crear una nueva Página.
3. Buscar y leer una Página.
4. Crear un nuevo Post (el sistema generará el autor automáticamente).
5. Buscar posts por título, categoría o autor.
6. Enviar y recibir mensajes entre usuarios.
7. Modificar datos del perfil, incluyendo avatar.
8. (Como Admin) eliminar un post desde el listado de Posts.
9. (Opcional) acceder al panel /admin para gestión directa.


