import pandas as pd
from pandas_jalali.converter import get_gregorian_date_from_jalali_date


import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import statsmodels.api as sm




new_data = pd.read_csv("new_data.csv")
print(new_data.head())
start = new_data['Log_Date'].min()
end = new_data['Log_Date'].max()
r = pd.date_range(start=new_data['Log_Date'].min(), end=new_data['Log_Date'].max())
new_data = new_data.drop("FROM", axis=1)
new_data = new_data.drop("TO", axis=1)
new_data = new_data.groupby(['Log_Date']).count().reset_index()
# new_data.reset_index()
print(new_data.head())
print("==========")
new_data = pd.DataFrame(np.array(new_data), columns=['Log_Date', 'Count'])
print(new_data.head())
print("==========")
new_data.set_index('Log_Date').reindex(r).fillna(0.0).rename_axis('Log_Date').reset_index()
print(new_data.head())

print("==================================")

# new_data['Log_Date'] = pd.to_datetime(new_data['Log_Date'], format='%Y/%m/%d')

# print(new_data)
# normilize data


# model

# specify training data
# define model configuration

# define model
# new_data = new_data.drop("FROM", axis=1)
# new_data = new_data.drop("TO", axis=1)

# print(new_data)
# new_data = new_data.values
# new_data2 = np.array(new_data)
# resDiff = sm.tsa.arma_order_select_ic(new_data, max_ar=5, max_ma=5, ic='aic', trend='c')
# print('ARMA(p,q) =',resDiff['aic_min_order'],'is the best.')
# print(np.asarray(new_data))
# new_data2 = new_data['Count'][start:end].dropna()
# new_data['year'] = new_data['Log_Date'].apply(lambda x: int(x.split("/")[0]))
# print(new_data)
# new_data = new_data.reset_index()
print('---------------->', new_data)
new_data.reset_index(drop=True, inplace=True)
ffff = pd.DataFrame(np.array(new_data), columns=['a', 'b'], index=False)
print('-------')
print(ffff)
arima = sm.tsa.statespace.SARIMAX(np.asarray(new_data), order=(72, 1, 7), seasonal_order=(0, 0, 0, 0))
#
# model_fit = model.fit()