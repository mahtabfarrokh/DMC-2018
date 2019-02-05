import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv", index_col=0)
# data.index = pd.to_datetime(data.index)
print(data.head())
data = data.drop("Departure_Time", axis=1)
data = data.drop("Departure_Date", axis=1)
data = data.drop("Price", axis=1)
data = data.drop("AL", axis=1)
print(len(data["Log_Date"]))
data.sort_values(["Log_Date", "FROM", "TO"], axis=0, ascending=True, inplace=True)
new_data = []
last_date = data["Log_Date"][0]
last_from = data["FROM"][0]
last_to = data["TO"][0]
last_count = 0
start = time.time()
print(data.head())
new_data = data.groupby(['Log_Date', 'FROM', 'TO'])['Log_Date'].count()
# print(new_data)
# new_data = pd.DataFrame(np.array(new_data), columns=["Log_Date", "FROM", "TO", "COUNT"])
# print(data.head())
new_data.to_csv("new_data.csv")
