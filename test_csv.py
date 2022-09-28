import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame

data = pandas.read_csv('data3.csv', usecols=['Cantidad', 'diametro'])
df =  DataFrame(data, columns=['Cantidad', 'diametro'])
df.plot(x='Cantidad', y='diametro', kind='line')
plt.show()

