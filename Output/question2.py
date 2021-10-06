# -*- coding: utf-8 -*-
"""Question2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iBmqkGHUx7GFL3yNMLPAO2wIThTMAUPa
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
df=pd.read_csv('main.csv')
result=df.groupby('occupation').agg({'age':['min','max']})
print(result)

from google.colab import files
result.to_csv('Answer2.csv')
files.download('Answer2.csv')