import pandas as pd
import os
from src.mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.mlProject.entity.config_entity import ModelTrainerConfig

""" 
joblib is a Python library used for efficiently serializing (saving) and deserializing (loading) Python objects, especially large data like NumPy arrays and machine learning models. It is commonly used in machine learning workflows to save trained models to disk and load them later for inference or further training.

Key uses:

Save and load scikit-learn models (joblib.dump, joblib.load)
Faster than pickle for large numerical data
"""
class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config=config
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        train_x=train_data.drop([self.config.target_column],axis=1)
        test_x=test_data.drop([self.config.target_column],axis=1)
        train_y=train_data[[self.config.target_column]]
        test_y=test_data[[self.config.target_column]]
        lr=ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        lr.fit(train_x,train_y)
        joblib.dump(lr,os.path.join(self.config.root_dir,self.config.model_name))