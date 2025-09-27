# Proyecto S3 Uploader Files

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Descripción

Este proyecto en Python permite subir archivos a Amazon S3 utilizando la librería **boto3**. 
Actualmente, el proyecto está diseñado para trabajar con archivos en formato **CSV**. 
La función load_csv ubicada en pipeline/load.py se encarga de: 
- Recibir como parámetro la **ruta del archivo** a cargar (no está limitada a una ruta fija).
- Leer el archivo CSV utilizando pandas y devolver un **DataFrame** que será luego procesado 
  por los siguientes pasos del pipeline (transformación, limpieza, guardado). 
  Este diseño modular permite desacoplar el origen del archivo del proceso de transformación. 
  Aunque inicialmente sólo se admite el formato CSV, la función está estructurada de forma que
  puede extenderse en el futuro para soportar otros tipos de archivos coomo JSON, Excel, etc,
  con mínimos cambios.

Buenas prácticas utilizadas:

- Uso de entornos virtuales
- Manejo seguro de credenciales con archivo `.env`
- Código limpio y modular

## 📁 Estructura del proyecto: 

La estructura del proyecto es la siguiente: 

```text
Proyecto-S3-Uploader/
│
├── .env                         # Variables de entorno (credenciales)
├── .gitignore                   # Archivos y carpetas excluidos del control de versiones
├── main.py                      # Script principal: orquesta la carga, transformación y subida a S3
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Lista de dependencias necesarias (pip install -r requirements.txt)
│
├── config/
│   └── settings.py              # Configuraciones generales del proyecto (paths, constantes, etc.)
│
├── data/
│   ├── input/
│   │   └── pacientes_crudo.csv  # Archivo de datos original (sin procesar)
│   └── output/
│       └── pacientes_procesado.csv  # Archivo de datos limpio y transformado
│
├── pipeline/
│   ├── load.py                  # Funciones para cargar los datos desde CSV
│   ├── save.py                  # Funciones para guardar los datos procesados y/o subir a S3
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
- Credenciales de AWS configuradas en un archivo `.env`  
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

Crea un archivo llamado .env en la raíz del proyecto con tus credenciales de AWS:

- AWS_ACCESS_KEY = your_access_key
- AWS_SECRET_ACCESS_KEY = your_secret_key
- AWS_REGION = your_region
- BUCKET_NAME = your_bucket_name

---

## 🚀 Uso

Para subir archivos a S3, simplemente ejecutá el script principal:

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

