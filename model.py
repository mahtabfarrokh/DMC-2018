import pandas as pd
import jalali

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import statsmodels.api as sm

new_data = pd.read_csv("new_data.csv")
for i in range(100) :
    new_data.loc[i,'Log_Date'] = jalali.Persian( new_data.loc[i,'Log_Date']).gregorian_string("{}/{}/{}")
    if i%100 == 0 :
       # print(jalali.Persian( new_data.loc[i,'Log_Date']).gregorian_string("{}/{}/{}"))
        print( new_data.loc[i,'Log_Date'] )
# print(new_data)

new_data = new_data[0:100]
print(new_data)
#plt.plot(new_data["Log_Date"], new_data["COUNT"])
#plt.show()
new_data['Log_Date'] = pd.to_datetime(new_data['Log_Date'],format='%Y/%m/%d')

print(new_data)
# print(new_data)
# normilize data



# model

# specify training data
# define model configuration

# define model
new_data = new_data.drop("FROM",axis = 1)
new_data = new_data.drop("TO",axis = 1)

print(new_data)
new_data2 = new_data.values
# new_data2 = np.array(new_data)
# resDiff = sm.tsa.arma_order_select_ic(new_data, max_ar=5, max_ma=5, ic='aic', trend='c')
# print('ARMA(p,q) =',resDiff['aic_min_order'],'is the best.')

arima = sm.tsa.statespace.SARIMAX(new_data,order=(72,1,7),freq='D',seasonal_order=(0,0,0,0),
                                  enforce_stationarity=False, enforce_invertibility=False,).fit
#
# model_fit = model.fit()


