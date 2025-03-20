import pandas as pd 
import numpy as np  
import time  
import gc  
import psutil  
import os

def load_data(filename, delimiter='\t'):
    return pd.read_csv(filename, delimiter=delimiter)

