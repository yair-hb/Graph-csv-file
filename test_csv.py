import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame

data = pandas.read_csv('data.csv', usecols=['date', 'price'])
df =  DataFrame(data, columns=['date', 'price'])
df.plot(x='date', y='price', kind='line')
plt.show()

