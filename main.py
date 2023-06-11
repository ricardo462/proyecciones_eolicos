from utils import *
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = 'data'

with cwd(PATH):
    files = os.listdir()
    file = 'esc_a.xlsx'
    esc_a = pd.read_excel(file, names=['date', 'bar', 'cost'])
    reales = pd.read_csv('costos_marginales_2022.csv', names=['date', 'wrong_cost', 'cost'], skiprows=1, sep=';')
    reales['cost'] = reales['cost'].apply(to_float)
    reales.drop('wrong_cost', inplace=True, axis=1)

esc_a['year'] = esc_a['date'].apply(get_projected_year)
esc_a['month'] = esc_a['date'].apply(get_projected_month)


reales['year'] = reales['date'].apply(get_year)
reales['month'] = reales['date'].apply(get_month)
reales['day'] = reales['date'].apply(get_day)
reales['hour'] = reales['date'].apply(get_hour)

#enero_01 = reales.loc[(reales['month'] == 1) & (reales['hour'] == 1)]
typical_days = []
means_per_month = []
for month in range(1, 13):
    costs_per_month = reales[reales['month'] == month]
    means_per_month.append(costs_per_month['cost'].mean())
    typical_days_per_month = []
    for hour in range(1, 25):
        costs_per_hour = reales[reales['hour'] == hour]
        costs = costs_per_hour['cost'].mean() 
        typical_days_per_month.append(costs)

    typical_days.append(typical_days_per_month)   

typical_days = np.array(typical_days)
means_per_month = np.array(means_per_month)


print(f'Largo de los días típicos: {typical_days.shape}')
print(f'Largo de las medias por mes: {means_per_month.shape}')

projected_mean = esc_a.loc[(esc_a['year'] == 2024) & (esc_a['month'] == 1)]['cost'].values[0]
estimated_mean = means_per_month[0]

print(f'Projected mean: {projected_mean}, estimated mean: {estimated_mean}')

# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots()
ax.plot(typical_days[0], label='Día típico 2022')
ax.plot(typical_days[0]/estimated_mean * projected_mean, label='Proyectada')
plt.title('Proyección del costo marginal del día típico de \n enero 2024 de versus día típico de enero de \n2022 según proyección de escenario A')
plt.xlabel('Hora')
plt.ylabel('Costo marginal $\\frac{USD}{MWh}$')
ax.legend()
plt.show()