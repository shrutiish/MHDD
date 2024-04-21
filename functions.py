import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv(r'C:\Users\SHRUTI\Desktop\MHDD\data\Mental health Depression disorder Data.csv')
df = pd.DataFrame(df, columns=df.columns)
df = df.drop("index",axis=1)
df

