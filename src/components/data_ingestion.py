import os
import sys
from src.exception import CustomeException
import src.logger as logger
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass



"""
We might need some inputs like where we might need to save training data and testing data
DataIngestionConfig class will helps to create those type of inputs.

"""

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv')



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initializing_data_ingestion(self):
        logger.info("Entered the data Ingestion class or component")

        try:
        
            df = pd.read_csv("notebook/data/stud.csv")
            logger.info("Reading dataframe") 
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

    
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=24)
            logger.info("Splitting the dataset into train and test")

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header = True)
            logger.info("The data is being saved in train and test file")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            

        except Exception as e :
            return CustomeException(e,sys)
        
if __name__ == "__main__":
    data_ingestion = DataIngestion()


