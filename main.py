from utils import *
import os
import pandas as pd

PATH = 'data'

with cwd(PATH):
    files = os.listdir()
    file = 'esc_a.xlsx'
    esc_a = pd.read_excel(file, names=['year', 'bar', 'cost'])
    reales = pd.read_csv('costos_marginales_2022.csv', names=['date', 'wrong_cost', 'cost'], skiprows=1, sep=';')
    reales['cost'] = reales['cost'].apply(to_float)
    reales.drop('wrong_cost', inplace=True, axis=1)



reales['year'] = reales['date'].apply(get_year)
reales['month'] = reales['date'].apply(get_month)
reales['day'] = reales['date'].apply(get_day)
reales['hour'] = reales['date'].apply(get_hour)

#enero_01 = reales.loc[(reales['month'] == 1) & (reales['hour'] == 1)]

for month in range(1, 13):
    costs_per_month = reales[reales['month'] == month]
    for hour in range(1, 25):
        costs_per_hour = reales[reales['hour'] == hour]
        costs = costs_per_hour['cost']  
        print(costs)
        print(costs.mean())
        break
    break




