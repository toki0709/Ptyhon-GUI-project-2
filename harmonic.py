import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('test.xlsx')

df.columns=['no.','harmonics1', 'harmonics2']
#print(df.head(48))

h1= df.iloc[1:48, 1]
h2 = df.iloc[1:48, 2]
#for i in range(0,49):
#for i in range(0,49):

plt.bar(h1,h2)
plt.show()