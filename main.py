from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>> stage{STAGE_NAME} started<<<<\n\n")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<< \n\n")
except Exception as e:
    logger.exception(e)

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<\n\n")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>{STAGE_NAME} completed<<<<<\n\n ")
except Exception as e:
    logger.exception(e)

STAGE_NAME="Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e