import pandas as pd 
import numpy as np  
import time  
import gc  
import psutil  
import os

def load_data(filename, delimiter='\t'):
    return pd.read_csv(filename, delimiter=delimiter)

def handle_missing_values(data):
    """Removing rows with missing values for T3 and T; for rows where only one value is missing, replace that missing T3 or T4 value with the mean for their Level group."""
    data = data.dropna(subset=['T3', 'T4'], how='all')
    data['T3'] = data['T3'].fillna(data.groupby('Level')['T3'].transform('mean')).round(1)
    data['T4'] = data['T4'].fillna(data.groupby('Level')['T4'].transform('mean')).round(1)
    return data
    
