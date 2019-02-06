import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import pandas as pd
from pandas_jalali.converter import get_gregorian_date_from_jalali_date


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
new_data['year'] = new_data['Log_Date'].apply(lambda x: int(x.split("/")[0]))
new_data['month'] = new_data['Log_Date'].apply(lambda x: int(x.split("/")[1]))
new_data['day'] = new_data['Log_Date'].apply(lambda x: int(x.split("/")[2]))
new_data['year_gregorian'], new_data['month_gregorian'], new_data['day_gregorian'] = \
    get_gregorian_date_from_jalali_date(new_data['year'], new_data['month'], new_data['day'])

new_data['year_gregorian'] = new_data['year_gregorian'].apply(lambda x: str(int(x)))
new_data['month_gregorian'] = new_data['month_gregorian'].apply(lambda x: str(int(x)))
new_data['day_gregorian'] = new_data['day_gregorian'].apply(lambda x: str(int(x)))

new_data['Log_Date'] = new_data['year_gregorian'] + '-' + new_data['month_gregorian'] + '-' + new_data['day_gregorian']
new_data['Log_Date'] = pd.to_datetime(new_data['Log_Date'])
print(new_data.head())
new_data = new_data.drop('year_gregorian', axis=1)
new_data = new_data.drop('month_gregorian', axis=1)
new_data = new_data.drop('day_gregorian', axis=1)
new_data = new_data.drop('year', axis=1)
new_data = new_data.drop('month', axis=1)
new_data = new_data.drop('day', axis=1)
print(new_data.head())
new_data.to_csv("new_data.csv", index=False)
