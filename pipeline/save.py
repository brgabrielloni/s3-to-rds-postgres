#--------------------------------------------------imports---------------------------------------------------

# importar módulo para interactuar con el S.O
import os

# importar módulo de pandas para trabajar con dataframes
import pandas as pd

# importar el archivo settings del módulo config para obtener las variables necesarias para crear el objetio S3
from config import settings

# importar la librería boto3, que es el SDK oficial de AWS para Python
import boto3

# importar create_engine de SQLAlchemy para crear conexiones con bases de datos relacionales y obtener metadatos
from sqlalchemy import create_engine, Table, MetaData

# mportar helper para construir INSERT con dialecto Postgres (soporta ON CONFLICT)
from sqlalchemy.dialects.postgresql import insert  

# importar objeto settings desde config.py para acceder a las variables de configuración del proyecto
from config import settings

# importar función personalizada get_logger desde utils/logger.py para manejar el registro de logs
from utils.logger import get_logger

#------------------------------------------------------------------------------------------------------------

# función que crea y devuelve un cliente de AWS S3 usando boto3 y las credenciales del archivo settings
logger = get_logger(__name__)

# función que guardar un Dataframe en una tabla de Postgres usando SQLAlchemy
def save_to_postgres(df: pd.DataFrame) -> None:
    try:
        logger.info("Conectando a la base de datos Postgres")

        # construir la URL de conexión
        url = (
            f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )
        engine = create_engine(url)

        # mantener solo las columnas que existen en la tabla destino
        columnas_validas = ["id", "nombre", "edad", "obra_social", "fecha_turno"]
        df = df[columnas_validas]

        # insertar datos en la tabla
        df.to_sql(settings.DB_TABLE, engine, if_exists="append", index=False)

        logger.info(f"{len(df)} registros insertados en {settings.DB_TABLE}.")

    except Exception as e:
        logger.exception(f"Error al guardar datos en Postgres: {e}")
        raise 

# función que inserta o actualiza datos de pacientes
def upsert_to_postgres_pacientes(df: pd.DataFrame):
    try:
        logger.info("Conectando a la base de datos Postgres")

        # Construir URL de conexión usando el dialecto postgresql+psycopg2
        url = (
            f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASS}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )

        # Crear el engine de SQLAlchemy
        engine = create_engine(url, pool_pre_ping=True)

        # Mantener solo las columnas válidas
        columnas_validas = ["id", "nombre", "edad", "obra_social", "fecha_turno"]
        df = df[columnas_validas].copy()

        # Reemplazar NaN por None (para que Postgres los inserte como NULL)
        df = df.where(pd.notnull(df), None)

        # Reflejar metadatos de la tabla
        metadata = MetaData(schema="clinica")
        metadata.reflect(bind=engine, only=["pacientes"])

        # Obtener el objeto Table
        table = metadata.tables["clinica.pacientes"]

        # Convertir DataFrame a lista de dicts
        registros = df.to_dict(orient="records")

        # Ejecutar un solo UPSERT en una transacción
        with engine.begin() as conn:
            stmt = insert(table).values(registros)
            stmt = stmt.on_conflict_do_update(
                index_elements=["id"],
                set_={c: stmt.excluded[c] for c in columnas_validas if c != "id"}
            )
            conn.execute(stmt)

        logger.info(f"{len(df)} registros upsertados en clinica.pacientes.")

    except Exception as e:
        logger.exception(f"Error al hacer UPSERT en clinica.pacientes: {e}")
        raise
