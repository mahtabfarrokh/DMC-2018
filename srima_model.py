from pandas import read_csv
import pandas as pd
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
import statsmodels.api as sm

number_of_dataset = 366
new_data2 = pd.read_csv("dataset/data" + str(i) + ".csv")
for i in range(number_of_dataset):

    print("-----------------------------------------------------------------",i)
    new_data = pd.read_csv("dataset/data"+str(i)+".csv",header=0, parse_dates=[0], index_col=0, squeeze=True)
    new_data2 = pd.read_csv("dataset/data" + str(i) + ".csv")

    if len(new_data) > 10:
        # print(new_data)
        start = new_data2["Log_Date"].min()
        end = new_data2["Log_Date"].max()

        print(start , end )
        # r = pd.date_range(start="4/13/2017", end="3/15/2018")
        # new_data.set_index('Log_Date').reindex(r).fillna(0.0).rename_axis('Log_Date').reset_index()
        test = read_csv('final_test.csv')
        new_data = new_data.drop("FROM", axis=1)
        new_data = new_data.drop("TO", axis=1)

        print(new_data)
        mod = sm.tsa.statespace.SARIMAX(new_data, trend='n', order=(1,1,1), seasonal_order=(0,0,0,12),enforce_stationarity = False , enforce_invertibility = False)
        results = mod.fit()

        # print (results.summary())
        forecast = results.predict(start = "4/13/2018" , end = "3/15/2019")
        # final_predict = []
        # for index, row in test.iterrows():
        #     final_predict.append(forecast[row["Log_Date"]])
        #

        print(forecast)
        # test["Sales"] = final_predict

        # test.to_csv("new_test.csv", index=False)

        # print(test)
