import pandas as pd
import numpy as np

data = pd.read_csv('1.supermarket.csv')

print('\nThe cols of the dataset:')
print(data.columns)

x = data.groupby('item_name')
x = x.sum()
print(x.head())