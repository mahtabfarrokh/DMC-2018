import pandas as pd
import numpy as np
import copy

# data = pd.read_csv("new_data.csv")
# print(data.head())
# new_data = data.groupby(['FROM', 'TO'])['Log_Date'].count()
# new_data =new_data.to_csv("temp.csv")
new_data = pd.read_csv("temp.csv")
data = pd.read_csv("new_data.csv")
print(new_data.head())
print("=======================")
counter = 0
res = []
for i in range(len(new_data['FROM'])):
    res.append([new_data['FROM'][i], new_data['TO'][i], counter])
    print(new_data['FROM'][i], new_data['TO'][i])
    s = data.loc[(data['FROM'] == new_data['FROM'][i]) & (data['TO'] == new_data['TO'][i])]
    s.to_csv("dataset/data" + str(counter)+".csv", index=False)
    counter += 1

pd.DataFrame(res, columns=['FROM','TO', 'FILE']).to_csv("to-from.csv", index=False)
for i in range(counter):
    s =pd.read_csv("dataset/data" + str(i)+".csv")
    s2 = copy.copy(s)
    s = s.drop("FROM", axis=1)
    s = s.drop("TO", axis=1)

    idx = pd.date_range(start=s2['Log_Date'].min(), end=s2['Log_Date'].max())
    s = pd.Series(s['COUNT'].values, index=s['Log_Date'])
    print(s.head())
    s.index = pd.DatetimeIndex(s.index)
    s = s.reindex(idx, fill_value=0)
    print(s.head())
    # f = pd.DataFrame(np.array(s), columns=['Log_Date', 'COUNT'])
    # from_1 = [s2['FROM'][i] for i in range(len)]
    # to_1 = [s2['TO'][i] for i in range(len(s.value))]
    s = pd.DataFrame({'Log_Date': s.index, 'COUNT': s.values})
    print(s.head())
    s.to_csv("dataset/dataa" + str(i) + ".csv", index=False)
    # for j
