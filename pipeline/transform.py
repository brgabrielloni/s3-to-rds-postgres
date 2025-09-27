#--------------------------------------------------imports---------------------------------------------------

# importar módulo de pandas para trabajar con dataframes
import pandas as pd

# importar módulo de fechas
from datetime import datetime

#importar función personalizada get_logger desde utils/logger.py para manejar el registro de logs
from utils.logger import get_logger

#------------------------------------------------------------------------------------------------------------

# función para limpiar el dataframe y normalizar valores
logger = get_logger(__name__)

# función que recibe un Dataframe y le aplica transformaciones, retornando un nuevo Dataframe modificado
def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    try:
        logger.info("Aplicando transformaciones a los datos")

        # Convertir columna fecha_turno a datetime (si no cumple el formato -> NaT)
        df["fecha_turno"] = pd.to_datetime(
            df["fecha_turno"],
            format="%d/%m/%Y",
            errors="coerce"  # valores inválidos quedan como NaT
        )

        # Rellenar nombres vacíos
        df["nombre"] = df["nombre"].fillna("DESCONOCIDO")

        # Rellenar otras columnas con valores por defecto
        df = df.fillna({
            "edad": 0,
            "obra_social": "No Informada"
        })

        logger.info("Transformaciones completadas.")
        return df

    except Exception as e:
        logger.exception(f"Error al transformar los datos: {e}")
        raise  

