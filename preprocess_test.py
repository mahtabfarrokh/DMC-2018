import pandas as pd
import numpy as np
from pandas_jalali.converter import get_gregorian_date_from_jalali_date

new_data = pd.read_csv("test.csv")
print(new_data.head())
new_data = new_data.drop('From', axis=1)
new_data = new_data.drop('To', axis=1)

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
new_data = new_data.drop('year_gregorian', axis=1)
new_data = new_data.drop('month_gregorian', axis=1)
new_data = new_data.drop('day_gregorian', axis=1)
new_data = new_data.drop('year', axis=1)
new_data = new_data.drop('month', axis=1)
new_data = new_data.drop('day', axis=1)
print(new_data.head())

new_data = new_data.groupby(['Log_Date']).count().reset_index()
new_data.to_csv('final_test.csv', index=False)
