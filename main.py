from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline

# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion_pipeline = DataIngestionTrainingPipeline()
#     data_ingestion_pipeline.initiate_data_ingestion()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "Data Transformation Stage"
# try:
#     logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_transformation_pipeline = DataTransformationTrainingPipeline()
#     data_transformation_pipeline.initiate_data_transformation()
#     logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e

def main():
    STAGE_NAME = "Model Trainer Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()