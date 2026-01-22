
    # data ingestion
import logging
import pandas as pd
import numpy as np


def data_ingestion():
    filename = r'C:\EnergyConsumption_Model\data\raw\Energy_consumption.csv'
    try:
        df = pd.read_csv(filename)
        logging.info("dataset successfully loaded")

    except:
        logging.info("check file path") 

    return df      