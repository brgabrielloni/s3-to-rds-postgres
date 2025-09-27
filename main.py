#--------------------------------------------------impports---------------------------------------------------
# importar la función read_csv_from_s3 del módulo pipeline.read 
from pipeline.read import read_csv_from_s3

## importar la función transform_data del módulo pipeline.transform que devolverá el dataframe procesado
from pipeline.transform import transform_data

## importar la función upsert_to_postgres_pacientes del módulo pipeline.save que guarda el archivo en una BD de Postgres RDS
from pipeline.save import upsert_to_postgres_pacientes

# importar del archivo logger que está en utils la variable logger
from utils.logger import get_logger

#-------------------------------------------------------------------------------------------------------------

logger = get_logger(__name__)

def main():
    logger.info("Iniciando pipeline ETL")
    df = read_csv_from_s3()
    df = transform_data(df)
    upsert_to_postgres_pacientes(df)
    logger.info("Pipeline finalizado con éxito.")

if __name__ == "__main__":
    main()

