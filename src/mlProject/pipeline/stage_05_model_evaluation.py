from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_evaluation import ModelEvaluation
from src.mlProject import logger

STAGE_NAME="Model Evaluation stage"
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(model_evaluation_config)
        model_evaluation_config.log_into_mlflow()

