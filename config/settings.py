#--------------------------------------------------imports---------------------------------------------------

# importar módulo para interactuar con el S.O
import os

# importar función load_dotenv del módulo dotenv para cargar las variables definidas en .env
from dotenv import load_dotenv 

#------------------------------------------------------------------------------------------------------------

# cargar variables de entorno desde el archivo .env
load_dotenv()

# obtener clave de acceso de AWS desde la variable definida en el archivo .env
AWS_ACCESS_KEY_ID   = os.getenv("AWS_ACCESS_KEY")

# obtener clave secreta de AWS desde la variable definida en el archivo .env
AWS_SECRET_ACCESS_KEY  = os.getenv('AWS_SECRET_ACCESS_KEY')

# obtener clave región de AWS desde la variable definida en el archivo .env
AWS_REGION = os.getenv('AWS_REGION')

# obtener el nombre del bucket de S3 de AWS desde la variable definida en el archivo .env
AWS_BUCKET  = os.getenv('BUCKET_NAME')

# obtener la ruta del archivo a procesar de S3 definida en el archivo .env
AWS_FILE_KEY = os.getenv("AWS_FILE_KEY")

# cargar variables de entorno de la BD de Postgres
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT")
DB_TABLE = os.getenv("DB_TABLE")


if not all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, AWS_BUCKET, AWS_FILE_KEY ]):
    raise ValueError ("No se cargaron todas las variables de entorno en el archivo .env")


