# Proyecto S3 to Postgres RDS

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Descripción

Este proyecto en Python implementa un pipeline ETL que permite leer archivos en formato CSV almacenados en Amazon S3, aplicar transformaciones de limpieza con pandas, y finalmente guardar los datos en una base de datos PostgreSQL alojada en Amazon RDS. 
El flujo principal es el siguiente:
- Conectarse a un bucket en S3 y descargar el archivo CSV indicado.
- Leer el archivo en un DataFrame de pandas para su procesamiento.
- Aplicar transformaciones de limpieza y normalización de datos (fechas, valores nulos, campos obligatorios).
- Insertar los registros en una tabla de Postgres en RDS, con manejo de logs para monitorear cada paso.

Buenas prácticas utilizadas:

- Separación de configuración y credenciales:
    Uso de variables de entorno (archivo .env) y módulo settings.py para no exponer claves sensibles en el código.
- Logging centralizado:
    Uso de utils/logger.py para registrar cada paso del pipeline, con distintos niveles (INFO, ERROR, EXCEPTION), lo que facilita la depuración y monitoreo.
- Validación de datos antes de la carga:
    Normalización de fechas, reemplazo de valores nulos y control de tipos de datos para asegurar consistencia antes de insertar en la base.
- Definición manual de esquemas y constraints en la BD:
    Tablas creadas con claves primarias y restricciones NOT NULL, garantizando integridad de datos y evitando depender de la creación automática de pandas.to_sql.
- Estructura modular del proyecto:
    División clara en carpetas (config/, pipeline/, utils/) para mantener un código más ordenado y escalable.
- Control de versiones con Git/GitHub:
    Uso de .gitignore para excluir archivos sensibles (.env, venv/, __pycache__/), manteniendo el repo limpio y seguro.
- Documentación del proyecto:
    README con descripción, instalación, uso y contacto, lo que facilita la comprensión y reutilización del proyecto por terceros.

Mejoras futuras:

- Automatización con AWS Lambda + S3 Triggers.
- Orquestación con Apache Airflow o AWS Step Functions.

## 📁 Estructura del proyecto: 

La estructura del proyecto es la siguiente: 

```text
s3-to_postgres_rds/
│
├── .env                         # Variables de entorno (credenciales)
├── .gitignore                   # Archivos y carpetas excluidos del control de versiones
├── main.py                      # Script principal: orquesta la carga, transformación y subida a S3
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Lista de dependencias necesarias (pip install -r requirements.txt)
│
├── config/
│   └── settings.py              # Configuración del proyecto
│
├── bd/
│   └──ddl.sql                   # Scripts SQL para creación de esquemas y tablas en Postgres RDS
│
├── pipeline/
│   ├── read.py                  # Funciones para leer datos de archivos almacenados en S3
│   ├── save.py                  # Funciones para guardar los datos procesados en Postgres RDS
│   └── transform.py             # Funciones de limpieza y transformación de datos
│
├── utils/
│   └── logger.py                # Configuración de logging para monitorear la ejecución
│
└── venv/                        # Entorno virtual de Python
```

---

## ✅ Requisitos

- Python 3.8 o superior  
- Credenciales de AWS y BD configuradas en un archivo `.env`  
- Entorno virtual para instalar las dependencias  

---

## ⚙️ Instalación

### 1. Crear y activar el entorno virtual:

En la terminal, dentro de la carpeta raíz del proyecto, ejecutá:

python -m venv venv

Luego activá el entorno virtual según tu sistema operativo:

🔹 Windows CMD:
    venv\Scripts\activate.bat

🔹 Windows PowerShell:
    .\venv\Scripts\activate

🔹 macOS / Linux:
    source venv/bin/activate

### 2. Instalar dependencias:

Con el entorno virtual activado, ejecutá:

pip install -r requirements.txt

### 3. Configurar archivo .env:

Crea un archivo llamado .env en la raíz del proyecto con tus credenciales de AWS y BD de RDS:

# BUCKET DE S3 de AWS:
- AWS_ACCESS_KEY = your_access_key
- AWS_SECRET_ACCESS_KEY = your_secret_key
- AWS_REGION = your_region
- BUCKET_NAME = your_bucket_name

# POSTGRES RDS:
- DB_HOST = your_database_host
- DB_USER= your_databse_user
- DB_PASS= your_database_password
- DB_PORT= your_database_port
- DB_TABLE= your_database_table_name

---

## 🚀 Uso

Para guardar los datos de tus archivos CSV de S3 en tablaS de Postgres RDS, simplemente ejecutá el script principal:

python main.py

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Si querés aportar, seguí estos pasos:

🔹 Hacé un fork del repositorio.

🔹 Creá una nueva rama para tu feature o bugfix:
    git checkout -b mi-nueva-funcionalidad
    
🔹Hacé commit de tus cambios con mensajes claros:
    git commit -m "Agrega nueva funcionalidad X"
    
🔹Enviá tu rama al repositorio remoto y abrí un Pull Request.

---

## 📬 Contacto

Si tenés preguntas o sugerencias, podés contactarme por:

✉️ E-mail: br.a.gabrielloni@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/braian-a-gabrielloni/

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT — ¡usalo, modificalo y compartilo libremente!

¡Gracias por visitar este proyecto! 

