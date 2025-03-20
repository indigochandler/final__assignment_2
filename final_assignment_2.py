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
    
def calculate_descriptive_statistics(data, columns):
    """Calculate descriptive statistics for specified columns."""
    descriptive_statistics = {}
    for column in columns:
        descriptive_statistics[column] = {
            "count": data[column].count(),
            "mean": round(data[column].mean(), 2),
            "std": round(data[column].std(), 2),
            "min": round(data[column].min(), 2),
            "25%": round(data[column].quantile(.25), 2),
            "50%": round(data[column].median(), 2),
            "75%": round(data[column].quantile(.75), 2),
            "max": round(data[column].max(), 2),
        }
    return pd.DataFrame(descriptive_statistics).round(2)

def identify_duplicates(data):
    duplicates = data[data.duplicated()]
    if len(duplicates) > 0:
        print(f"Number of repeated rows: {len(duplicates)}")
        print("Repeated rows:")
        duplicates = data[data.duplicated(keep=False)]
        print(duplicates)
    else:
        print("No repeated rows found.")
    return duplicates
