# Task Manager IA 🤖

**Gestor de tareas inteligente desarrollado en Python**, con persistencia de datos en JSON e integración con la API de OpenAI para descomponer tareas complejas en subtareas simples y accionables.

El proyecto combina programación orientada a objetos, gestión de archivos, consumo de APIs externas y pruebas automatizadas, a través de una aplicación de consola.

## 📋 Descripción general

Task Manager IA permite organizar y administrar tareas desde una interfaz de línea de comandos (CLI).

Además de las operaciones tradicionales de un gestor de tareas, incorpora inteligencia artificial para transformar actividades complejas en pasos más pequeños y fáciles de ejecutar.

### Funcionalidades principales

- Crear tareas individuales.
- Listar las tareas existentes.
- Marcar tareas como completadas.
- Eliminar tareas mediante su identificador.
- Guardar y recuperar tareas automáticamente en formato JSON.
- Generar subtareas a partir de una tarea compleja utilizando OpenAI.
- Mantener la información entre ejecuciones del programa.
- Verificar las funcionalidades principales mediante pruebas automatizadas.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Propósito |
|---|---|
| Python 3.12 | Lenguaje principal de desarrollo |
| Programación orientada a objetos | Organización de clases, atributos y métodos |
| JSON | Persistencia local de tareas |
| OpenAI API | Generación inteligente de subtareas |
| python-dotenv | Carga de variables de entorno |
| pytest | Ejecución de pruebas automatizadas |
| Git | Control de versiones |
| GitHub | Alojamiento del código fuente |

La aplicación utiliza principalmente bibliotecas estándar de Python, junto con dependencias externas para la integración de inteligencia artificial y las pruebas automatizadas.

---

## ⚙️ Funcionalidades

### 1. Gestión básica de tareas

El sistema permite realizar operaciones sobre una colección de tareas:

- **Añadir:** crear una tarea con una descripción y un identificador.
- **Listar:** consultar las tareas registradas y su estado.
- **Completar:** marcar una tarea como finalizada mediante su ID.
- **Eliminar:** eliminar una tarea existente.
- **Persistir:** guardar automáticamente los cambios.

Cada tarea es representada mediante una instancia de la clase `Task`.

### 2. Persistencia de datos con JSON

Las tareas se almacenan localmente en `tasks.json`, evitando que la información se pierda al cerrar el programa.

Ejemplo de estructura:

```json
[
    {
        "id": 1,
        "description": "Estudiar Python",
        "completed": false
    },
    {
        "id": 2,
        "description": "Practicar Git",
        "completed": true
    }
]
```

Cada objeto contiene:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | int | Identificador de la tarea |
| `description` | str | Descripción de la actividad |
| `completed` | bool | Indica si la tarea está completada |

La lectura y escritura de datos se realizan mediante las funciones `json.load()` y `json.dump()` de Python.

### 3. Generación de subtareas con inteligencia artificial

La aplicación incorpora una funcionalidad para dividir tareas complejas utilizando la API de OpenAI.

El usuario proporciona una descripción y el sistema solicita al modelo una lista de actividades más pequeñas.

**Ejemplo ilustrativo:**

```text
Descripción de la tarea compleja:
Desarrollar una aplicación web

Subtareas generadas:

1. Definir los requisitos de la aplicación.
2. Diseñar la estructura del proyecto.
3. Crear la interfaz de usuario.
4. Implementar la lógica del backend.
5. Configurar el almacenamiento de datos.
6. Realizar pruebas de funcionamiento.
```

Las subtareas generadas se incorporan al gestor como tareas individuales.

La integración se encuentra implementada en `ai_service.py`.

**Nota:** esta funcionalidad requiere una API Key válida, conectividad a internet y créditos disponibles en la cuenta de OpenAI. Su utilización puede generar costos según el modelo y el volumen de tokens consumidos.

---

## 📁 Estructura del proyecto

```text
Taskmanager/
│
├── main.py
│   └── Interfaz de consola y menú principal
│
├── task_manager.py
│   └── Clases Task y TaskManager
│
├── ai_service.py
│   └── Integración con la API de OpenAI
│
├── tests/
│   └── test_task_manager.py
│       └── Pruebas automatizadas con pytest
│
├── requirements.txt
│   └── Dependencias del proyecto
│
├── .gitignore
│   └── Archivos excluidos del control de versiones
│
└── README.md
    └── Documentación del proyecto
```

### Archivos locales

Durante la ejecución también pueden existir:

```text
.env
tasks.json
.venv/
__pycache__/
.pytest_cache/
```

Estos archivos y directorios se utilizan localmente y se excluyen del repositorio mediante `.gitignore`.

- `.env`: contiene variables de entorno y credenciales.
- `tasks.json`: almacena las tareas del usuario.
- `.venv/`: contiene el entorno virtual de Python.
- `__pycache__/`: contiene archivos generados por Python.
- `.pytest_cache/`: almacena información temporal de pytest.

---

## 📦 Requisitos previos

Para ejecutar la aplicación se necesita:

- Python 3.10 o superior.
- Git, si se desea clonar el repositorio.
- Acceso a una terminal.
- Conexión a internet para utilizar las funciones de IA.
- Una API Key de OpenAI para generar subtareas inteligentes.

El gestor básico de tareas puede utilizarse sin configurar OpenAI.

---

## 🚀 Instalación

### 1. Clonar el repositorio

Ejecutar desde una terminal:

```bash
git clone https://github.com/CristianBoto/TaskManager.git
```

Ingresar al directorio:

```bash
cd TaskManager
```

### 2. Crear un entorno virtual

```powershell
python -m venv .venv
```

El entorno virtual permite mantener las dependencias del proyecto aisladas de otras instalaciones de Python.

### 3. Activar el entorno virtual

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux o macOS:**

```bash
source .venv/bin/activate
```

Cuando esté activado, la terminal mostrará generalmente el prefijo `(.venv)`.

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Esto instala las bibliotecas declaradas en el archivo de dependencias.

Para ejecutar las pruebas automatizadas, también debe estar instalado `pytest`:

```powershell
python -m pip install pytest
```

---

## 🔐 Configuración de OpenAI

Para utilizar la generación de subtareas con inteligencia artificial, es necesario configurar una API Key.

### 1. Obtener una API Key

Acceder a:

https://platform.openai.com/api-keys

Crear una clave desde la plataforma oficial de OpenAI.

### 2. Crear el archivo `.env`

En la raíz del proyecto, crear un archivo llamado `.env`.

Agregar:

```env
OPENAI_API_KEY=tu_clave_aqui
```

Reemplazar `tu_clave_aqui` por la clave correspondiente.

### 3. Seguridad

La API Key es una credencial privada.

**No debe compartirse, publicarse ni incorporarse al código fuente.**

El archivo `.env` debe estar excluido de Git mediante `.gitignore`.

Ejemplo:

```gitignore
.env
.venv/
__pycache__/
.pytest_cache/
tasks.json
```

### 4. Cargar la variable en Python

El proyecto utiliza variables de entorno para acceder a la clave sin incluirla directamente en el código.

Ejemplo:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

La función `load_dotenv()` carga las variables definidas en `.env`, mientras que `os.getenv()` permite recuperar el valor de `OPENAI_API_KEY`.

---

## ▶️ Ejecutar la aplicación

Desde la raíz del proyecto, con el entorno virtual activado:

```powershell
python main.py
```

### Menú principal

La aplicación presenta un menú interactivo:

```text
--- Gestor de Tareas Inteligente ---

1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

Elige una opción:
```

El usuario selecciona una opción ingresando el número correspondiente.

---

## 🧩 Arquitectura y funcionamiento

La aplicación se organiza en tres módulos principales.

### `task_manager.py`

Contiene la lógica del gestor.

**Clase `Task`**

Representa una tarea individual mediante los siguientes atributos:

- `id`: identificador.
- `description`: descripción.
- `completed`: estado de finalización.

También implementa `__str__()` para proporcionar una representación legible de cada tarea.

**Clase `TaskManager`**

Administra la colección de tareas y sus operaciones principales.

Métodos:

| Método | Función |
|---|---|
| `__init__()` | Inicializa el gestor y carga los datos existentes |
| `add_task()` | Crea y registra una nueva tarea |
| `list_tasks()` | Muestra las tareas existentes |
| `complete_task()` | Marca una tarea como completada |
| `delete_task()` | Elimina una tarea |
| `save_tasks()` | Guarda las tareas en JSON |
| `load_tasks()` | Recupera las tareas almacenadas |

### `main.py`

Implementa la interfaz de línea de comandos.

Sus responsabilidades incluyen:

- Mostrar el menú principal.
- Recibir las opciones seleccionadas.
- Solicitar los datos necesarios.
- Ejecutar las operaciones del gestor.
- Conectar la funcionalidad de generación de subtareas con IA.

### `ai_service.py`

Centraliza la comunicación con la API de OpenAI.

Se encarga de:

1. Recibir la descripción de una tarea compleja.
2. Preparar los mensajes enviados al modelo.
3. Realizar la petición a la API.
4. Obtener la respuesta generada.
5. Procesar el texto recibido.
6. Convertir los resultados en una lista de subtareas.

La separación de responsabilidades facilita el mantenimiento y la ampliación del proyecto.

---

## 💾 Flujo de persistencia

### Crear una tarea

Cuando el usuario añade una tarea:

1. Se recibe la descripción.
2. Se crea un objeto `Task`.
3. Se asigna un identificador.
4. La tarea se añade a la lista interna.
5. Se actualiza el siguiente identificador disponible.
6. Se guarda la información en el archivo JSON.

### Cargar tareas

Cuando se inicia el programa:

1. Se inicializa el objeto `TaskManager`.
2. Se ejecuta `load_tasks()`.
3. Se recuperan los datos existentes del archivo JSON.
4. Los diccionarios se convierten en objetos `Task`.
5. Se determina el siguiente identificador.

Si todavía no existe el archivo de tareas, el gestor puede comenzar con una colección vacía.

### Completar o eliminar tareas

Cuando se modifica o elimina una tarea, el gestor actualiza su colección interna y vuelve a guardar el estado.

De esta manera, los cambios persisten entre ejecuciones.

---

## 🧪 Pruebas automatizadas

El proyecto utiliza **pytest** para verificar el comportamiento de las funcionalidades principales.

Las pruebas están organizadas en:

```text
tests/
└── test_task_manager.py
```

### Funcionalidades verificadas

La suite incluye seis pruebas:

| Prueba | Objetivo |
|---|---|
| `test_add_task_creates_and_saves_new_task` | Verificar la creación y persistencia de una tarea |
| `test_list_tasks_prints_each_task` | Verificar el listado de tareas |
| `test_complete_task_marks_task_as_completed` | Verificar el cambio de estado |
| `test_delete_task_removes_task_from_list_and_file` | Verificar la eliminación y persistencia |
| `test_save_tasks_writes_json_to_file` | Verificar la escritura en JSON |
| `test_load_tasks_restores_tasks_from_file` | Verificar la recuperación de datos |

### Ejecutar las pruebas

Desde la raíz del proyecto:

```powershell
python -m pytest -v
```

También se pueden ejecutar en modo resumido:

```powershell
python -m pytest -q
```

### Resultado de referencia

En la última comprobación realizada durante el desarrollo:

```text
6 passed in 0.11s
```

Las seis pruebas finalizaron correctamente.

### Aislamiento de las pruebas

Las pruebas utilizan herramientas de pytest:

- `tmp_path`: proporciona rutas temporales para trabajar con archivos de prueba.
- `monkeypatch`: permite modificar temporalmente configuraciones o atributos durante la ejecución de un test.

Estas herramientas evitan que las pruebas alteren el archivo real `tasks.json`.

**Importante:** la ejecución exitosa de las seis pruebas confirma los escenarios evaluados, pero no garantiza que la aplicación esté libre de errores en todos los casos.

---

## 🔒 Consideraciones técnicas y limitaciones

El proyecto tiene actualmente las siguientes características y limitaciones:

- Es una aplicación de consola, sin interfaz gráfica.
- Utiliza almacenamiento local basado en JSON.
- No utiliza una base de datos relacional.
- No incorpora un sistema de autenticación.
- La generación de subtareas depende de la disponibilidad de la API de OpenAI.
- El uso de la API puede generar costos.
- Las pruebas automatizadas actuales se concentran en la lógica de `TaskManager`.
- Todavía se pueden ampliar las pruebas para cubrir errores, entradas inválidas y fallas de servicios externos.

El sistema está diseñado principalmente como un proyecto de aprendizaje y experimentación.

---

## 📈 Mejoras futuras

Entre las posibles funcionalidades a incorporar se encuentran:

### Gestión de tareas

- Incorporar fecha de creación y vencimiento.
- Añadir niveles de prioridad.
- Permitir categorías o etiquetas.
- Filtrar tareas por estado.
- Implementar búsquedas por descripción.
- Agregar un historial de tareas completadas y eliminadas.

### Inteligencia artificial

- Generar subtareas con diferentes niveles de detalle.
- Incorporar estimaciones de duración.
- Mejorar el tratamiento de errores de la API.
- Implementar respuestas estructuradas en JSON.
- Permitir sugerencias para organizar y priorizar actividades.

### Arquitectura

- Incorporar una base de datos SQLite o PostgreSQL.
- Desarrollar una API REST con FastAPI.
- Añadir una interfaz web.
- Separar configuraciones según el entorno.
- Incorporar registros de errores y eventos.

### Calidad de software

- Ampliar la cobertura de pruebas.
- Agregar tests para casos excepcionales.
- Implementar pruebas de integración de la funcionalidad con IA.
- Incorporar herramientas de análisis estático.
- Configurar GitHub Actions para ejecutar las pruebas automáticamente.

---

## 🎯 Objetivo del proyecto

Task Manager IA fue desarrollado como ejercicio práctico para aplicar e integrar conocimientos de desarrollo de software.

Los principales conceptos trabajados son:

- Programación orientada a objetos en Python.
- Diseño de clases y métodos.
- Estructuras de datos.
- Lectura y escritura de archivos.
- Persistencia de información mediante JSON.
- Gestión de dependencias y entornos virtuales.
- Consumo de APIs externas.
- Integración de modelos de inteligencia artificial.
- Gestión segura de credenciales.
- Pruebas automatizadas con pytest.
- Control de versiones con Git y GitHub.

El proyecto busca consolidar estos conocimientos mediante una aplicación funcional, modular y extensible.

---

## 👨‍💻 Autor

**Cristian Damián Boto**

GitHub: [CristianBoto](https://github.com/CristianBoto)

Repositorio: [TaskManager](https://github.com/CristianBoto/TaskManager)

---

## 📄 Estado del proyecto

**En desarrollo.**

La versión actual permite administrar tareas desde consola, almacenarlas localmente y generar subtareas mediante inteligencia artificial.

Se continuará ampliando el proyecto con nuevas funcionalidades, mejoras técnicas y mayor cobertura de pruebas.