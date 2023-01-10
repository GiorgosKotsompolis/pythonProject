import pandas
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('1.supermarket.csv')
print(data)

temp = data.groupby('item_name')['quantity'].sum()
print("temp is:")
print(temp)
print(type(temp))
#q = data.groupby('item_name').quantity.sum()

#plt.bar(q.index, q)
#plt.show()