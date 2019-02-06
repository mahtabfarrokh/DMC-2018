from pandas import read_csv
import pandas as pd
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
import statsmodels.api as sm
import numpy as np
import math

number_of_dataset = 366
result_list = []
to_from = pd.read_csv('to-from.csv')
final_test = pd.read_csv('final_test.csv')

for i in range(number_of_dataset):

    print("-----------------------------------------------------------------", i)
    new_data = pd.read_csv("dataset/dataa"+str(i)+".csv",header=0, parse_dates=[0], index_col=0, squeeze=True)
    new_data2 = pd.read_csv("dataset/dataa" + str(i) + ".csv")
    if len(new_data) > 10:
        # print(new_data)
        start = new_data2["Log_Date"].min()
        end = new_data2["Log_Date"].max()

        # print(start , end )
        # r = pd.date_range(start="4/13/2017", end="3/15/2018")
        # new_data.set_index('Log_Date').reindex(r).fillna(0.0).rename_axis('Log_Date').reset_index()
        test = read_csv('final_test.csv')
        # new_data = new_data.drop("FROM", axis=1)
        # new_data = new_data.drop("TO", axis=1)

        # print(new_data)
        mod = sm.tsa.statespace.SARIMAX(new_data, trend='n', order=(1,1,1), seasonal_order=(0,0,0,12),enforce_stationarity = False , enforce_invertibility = False)
        results = mod.fit()
        result_list.append(results)
        # print (results.summary())
        # forecast = results.predict(start="2018-03-21", end="2018-03-21")
        # forecast_list.append(forecast)
        # final_predict = []
        # for index, row in test.iterrows():
        #     final_predict.append(forecast[row["Log_Date"]])
        #

        # print(forecast)
        # test["Sales"] = final_predict

        # test.to_csv("new_test.csv", index=False)

        # print(test)
    else:
        result_list.append(0)

c = 0
fiiiiinaaaal = []
fiiiiinaaaal2 = []
fiiiiinaaaal3 = []
fiiiiinaaaal4 = []
print("predict : +++++++++++++++++++++++++++++++++++++++++++++++")
print(len(final_test['To']))
# len(final_test['To'])

for i in range(len(final_test['To'])):
    flag = False
    for j in range(c, len(to_from['TO'])):
        if to_from['TO'][j] == final_test['To'][i] and to_from['FROM'][j] == final_test['From'][i]:
            c = j
            index_found = to_from['FILE'][j]
            print("===>")
            print(len(result_list), j , len(to_from['TO']))
            if result_list[j] == 0:
                fiiiiinaaaal.append(0)
                fiiiiinaaaal2.append(final_test['Log_Date'][i])
                fiiiiinaaaal3.append(final_test['From'][i])
                fiiiiinaaaal4.append(final_test['To'][i])
                flag = True
                print("=======================================================")
                print(0)
            else:
                try:
                    forecast = result_list[j].predict(start=final_test['Log_Date'][i], end=final_test['Log_Date'][i])
                    flag = True
                    print("=======================================================")
                    r = str(int((float(str(forecast).split(" ")[4].split("\n")[0]))))
                    print(r)
                    fiiiiinaaaal.append(r)
                    fiiiiinaaaal2.append(final_test['Log_Date'][i])
                    fiiiiinaaaal3.append(final_test['From'][i])
                    fiiiiinaaaal4.append(final_test['To'][i])
                except KeyError:
                    fiiiiinaaaal.append(0)
                    fiiiiinaaaal2.append(final_test['Log_Date'][i] )
                    fiiiiinaaaal3.append(final_test['From'][i])
                    fiiiiinaaaal4.append(final_test['To'][i])
                    flag = True
                    print("=======================================================")
                    print(0)
            break
    if not flag:
        fiiiiinaaaal.append(0)
        fiiiiinaaaal2.append(final_test['Log_Date'][i])
        fiiiiinaaaal3.append(final_test['From'][i])
        fiiiiinaaaal4.append(final_test['To'][i])
        flag = False
        print("=======================================================")
        print(0)
    else:
        flag = False



print(len(fiiiiinaaaal))
x =pd.DataFrame(np.array(fiiiiinaaaal))
x2 =pd.DataFrame(np.array(fiiiiinaaaal2))
x3 =pd.DataFrame(np.array(fiiiiinaaaal3))
x4 =pd.DataFrame(np.array(fiiiiinaaaal4))
print(x.head())
x.to_csv('final.csv', index=False)
x2.to_csv('final2.csv', index=False)
x3.to_csv('final3.csv', index=False)
x4.to_csv('final4.csv', index=False)










