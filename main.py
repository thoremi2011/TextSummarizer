from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline
from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline

def main():
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Data Transformation Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation_pipeline = DataTransformationTrainingPipeline()
        data_transformation_pipeline.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Model Trainer Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer_pipeline = ModelTrainerPipeline()
        model_trainer_pipeline.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

    STAGE_NAME = "Model Evaluation Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()


# from src.textSummarizer.logging import logger
# from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
# from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
# from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline
# from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline

# def execute_stage(stage_name, stage_callable):
#     try:
#         logger.info(f">>>>>> stage {stage_name} started <<<<<<")
#         stage_callable()
#         logger.info(f">>>>>> stage {stage_name} completed <<<<<<")
#     except Exception as e:
#         logger.exception(f"Error during {stage_name}: {e}")
#         # Optionally, continue execution instead of raising the exception.
#         # raise e

# def main():
#     stages = [
#         ("Data Ingestion Stage", lambda: DataIngestionTrainingPipeline().initiate_data_ingestion()),
#         ("Data Transformation Stage", lambda: DataTransformationTrainingPipeline().initiate_data_transformation()),
#         ("Model Trainer Stage", lambda: ModelTrainerPipeline().initiate_model_trainer()),
#         ("Model Evaluation Stage", lambda: ModelEvaluationPipeline().initiate_model_evaluation()),
#     ]
    
#     for stage_name, stage_callable in stages:
#         execute_stage(stage_name, stage_callable)

# if __name__ == "__main__":
#     from multiprocessing import freeze_support
#     freeze_support()
#     main()
