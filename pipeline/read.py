#--------------------------------------------------imports---------------------------------------------------

# importar módulo de pandas para trabajar con dataFrames
import boto3

# importar módulo de pandas para trabajar con DataFrames
import pandas as pd  

# importar módulo estándar de Python para manejar flujos de entrada/salida en memoria
import io  

# importar objeto de configuración definido en el archivo config.py 
from config import settings  

# importar función personalizada para inicializar el logger desde utils/logger.py
from utils.logger import get_logger  

#------------------------------------------------------------------------------------------------------------

# función que lee el archivo de S3 y lo guarda como dataframe

logger = get_logger(__name__)

# función que lee un archivo CSV desde un bucket de S3 y lo devuelve como DataFrame de pandas.
def read_csv_from_s3() -> pd.DataFrame:
    try:
        # Crear cliente de S3 con credenciales desde settings
        logger.info("Conectando a S3...")
        s3_client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )

        # Obtener el archivo desde el bucket y leerlo como DataFrame
        obj = s3_client.get_object(Bucket=settings.AWS_BUCKET, Key=settings.AWS_FILE_KEY)
        df = pd.read_csv(io.BytesIO(obj["Body"].read()))

        # Log de éxito con la cantidad de filas
        logger.info(f"Archivo {settings.AWS_FILE_KEY} leído desde S3 con {len(df)} filas.")
        return df

    except Exception as e:
        # Captura cualquier error inesperado y lo registra
        logger.exception(f"Error al leer el archivo {settings.AWS_FILE_KEY} desde S3: {e}")
        raise  

