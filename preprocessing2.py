import pandas as pd
import numpy as np


# data = pd.read_csv("new_data.csv")
# print(data.head())
# new_data = data.groupby(['FROM', 'TO'])['Log_Date'].count()
# new_data =new_data.to_csv("temp.csv")
new_data = pd.read_csv("temp.csv")
data = pd.read_csv("new_data.csv")
print(new_data.head())
print("=======================")
for i in range(len(new_data['FROM'])):
    print(new_data['FROM'][i], new_data['TO'][i])
    s = data.loc[(data['FROM'] == new_data['FROM'][i]) & (data['TO'] == new_data['TO'][i])]
    s.to_csv("dataset/data" + str("-") + str(new_data['FROM'][i]) + str("-")+ str(new_data['TO'][i])+".csv", index=False)
