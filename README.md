# 📝 Aplicación Web de Tareas Pendientes (Python - Django)

Una aplicación web completa y funcional desarrollada con **Python y Django** para la gestión eficiente de tareas personales. Este proyecto representa la culminación del aprendizaje enfocado en el desarrollo Backend puro, implementando una arquitectura sólida, seguridad básica y operaciones de base de datos.

## ✨ Características Principales

* **Autenticación de Usuarios:** Sistema completo de Login y Logout. Cada usuario tiene una sesión segura y aislada.
* **Privacidad de Datos:** Implementación de `LoginRequiredMixin` para garantizar que un usuario no registrado no pueda acceder a las URL de la aplicación.
* **Operaciones CRUD:** * **C**reate: Creación de nuevas tareas mediante formularios de Django.
  * **R**ead: Visualización de lista completa y detalles individuales de cada tarea.
  * **U**pdate: Edición y actualización del estado de las tareas.
  * **D**elete: Eliminación segura con pantalla de confirmación.
* **Arquitectura Limpia:** Uso intensivo de **Class-Based Views** (Vistas basadas en clases) para mantener un código `views.py` modular, legible y fácil de escalar.
* **Seguridad:** Protección contra vulnerabilidades de falsificación de peticiones en sitios cruzados mediante etiquetas `{% csrf_token %}` en todos los formularios.
* **Interfaz de Usuario (UI):** Diseño refactorizado extrayendo estilos en línea a archivos `.css` puros para una carga más rápida y un mantenimiento más sencillo.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.10+, Django 5.x
* **Base de Datos:** SQLite3 (Integrada en la fase de desarrollo)
* **Frontend:** HTML5, CSS3, Django Templates

## 🧠 Retos Superados y Aprendizaje

Durante el desarrollo de este proyecto, no solo se escribió código, sino que se abordaron problemas de infraestructura reales:
* **Gestión de Entornos Aislados:** Configuración manual de variables de entorno (PATH) en Windows, deshabilitación de alias conflictivos del SO y despliegue de una "sala blanca" virtual (`entorno_prueba`) para evitar colisiones de dependencias.
* **Estrategia de Paralelismo Escalonado:** Foco absoluto en dominar la lógica de Python y el flujo MVT (Model-View-Template) de Django como paso previo antes de escalar a consultas complejas con SQL.

## 🚀 Cómo ejecutar este proyecto localmente

Si deseas clonar y probar este proyecto en tu propia máquina, sigue estos pasos:

1. **Clona el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo
   
2. **Crea y activa un entorno virtual limpio:**
```bash
   python -m venv entorno_prueba
  # En Windows:
  .\entorno_prueba\Scripts\activate
```
3. **Instala Django:**
```bash
   pip install django
```
4. **Aplica las migraciones (Para crear tu propia base de datos local):**
```bash
   cd src\proyecto
   python manage.py migrate
```
5. **Inicia el servidor de desarrollo:**
```bash
   python manage.py runserver
   Y visita en tu navegador la dirección: http://127.0.0.1:8000/
```
