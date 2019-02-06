import pandas as pd
from pandas_jalali.converter import get_gregorian_date_from_jalali_date


import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import statsmodels.api as sm


new_data = pd.read_csv("new_data.csv")
print(new_data.head())

# plt.plot(new_data["Log_Date"], new_data["COUNT"])
# plt.show()




new_data['Log_Date'] = pd.to_datetime(new_data['Log_Date'], format='%Y/%m/%d')

print(new_data)
# print(new_data)
# normilize data


# model

# specify training data
# define model configuration

# define model
new_data = new_data.drop("FROM", axis=1)
new_data = new_data.drop("TO", axis=1)

print(new_data)
new_data2 = new_data.values
# new_data2 = np.array(new_data)
# resDiff = sm.tsa.arma_order_select_ic(new_data, max_ar=5, max_ma=5, ic='aic', trend='c')
# print('ARMA(p,q) =',resDiff['aic_min_order'],'is the best.')

arima = sm.tsa.statespace.SARIMAX(new_data, order=(72, 1, 7), freq='D', seasonal_order=(0, 0, 0, 0),
                                  enforce_stationarity=False, enforce_invertibility=False, ).fit
#
# model_fit = model.fit()
