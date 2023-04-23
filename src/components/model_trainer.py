import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRFRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

@dataclass
class ModelTrainterConfig():
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer():
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainterConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1], 
                train_arr[:, -1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            #create dictionary of models

            models = {
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-Neighbours Regressor" : KNeighborsRegressor(),
                "XGBRegressor" : XGBRFRegressor(),
                "Cat Boost Rergressor" : CatBoostRegressor(verbose=False),
                "Ada Boost Regressor" : AdaBoostRegressor()

            }

            model_report : dict = evaluate_model(X_train = X_train, y_train = y_train, X_test = X_test, y_test = y_test 
                                                 ,models = models)
            
            # to get the best model score  from the dict

            best_model_score = max(model_report.values())

            # to get the best model name from the  dict

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info(f"best model found  on both training and testing dataset")

            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )
            y_pred_test = best_model.predict(X_test)
            r2_square = r2_score(y_test, y_pred_test)
            return best_model, r2_square
        
        except Exception as e:
            raise CustomException(e, sys)

