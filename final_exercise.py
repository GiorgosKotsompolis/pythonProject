import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data_final_exercise.csv')
zip = data.groupby('zip_code')
#print(zip.first())

agg_zip = zip.aggregate(np.sum)

bottles_sold = agg_zip['bottles_sold']

print(bottles_sold)

plt.plot(bottles_sold,'o')
plt.xlabel("Total_Bottles_Sold")
plt.ylabel("Zip_Code")
plt.show()

