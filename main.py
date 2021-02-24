#Desc: Dual Moving average cross over to determine transactions

#libraries

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot  as plt
plt.style.use('fivethirtyeight')

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0] 
rel_path = "sample_data/appl.csv"
abs_file_path = os.path.join(script_dir, rel_path)

#Read file
APPL_data = open(rel_path, 'r')

#Store data 
APPL_data = pd.read_csv('appl.csv')

