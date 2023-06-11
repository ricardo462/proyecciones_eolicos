from utils import *
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = 'data'
SCENARIO_FILE = 'esc_a.xlsx'
SCENARIO_A_FILE = 'esc_a.xlsx'
SCENARIO_B_FILE = 'esc_b.xlsx'
SCENARIO_C_FILE = 'esc_c.xlsx'
SCENARIO_D_FILE = 'esc_d.xlsx'
SCENARIO_E_FILE = 'esc_e.xlsx'
REAL_COSTS_FILE = 'costos_marginales_2022.csv'

with cwd(DATA_PATH):    
    scenario_a = get_scenario(SCENARIO_A_FILE)
    scenario_b = get_scenario(SCENARIO_B_FILE)
    scenario_c = get_scenario(SCENARIO_C_FILE)
    scenario_d = get_scenario(SCENARIO_D_FILE)
    scenario_e = get_scenario(SCENARIO_E_FILE)

    reales = get_real_costs(REAL_COSTS_FILE)
    

# Calcular promedios 2022
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


year = 2025
projected_month = 3

projected_mean_a = scenario_a.loc[(scenario_a['year'] == year) & (scenario_a['month'] == projected_month)]['cost'].values[0]
projected_mean_b = scenario_b.loc[(scenario_b['year'] == year) & (scenario_b['month'] == projected_month)]['cost'].values[0]
projected_mean_c = scenario_c.loc[(scenario_c['year'] == year) & (scenario_c['month'] == projected_month)]['cost'].values[0]
projected_mean_d = scenario_d.loc[(scenario_d['year'] == year) & (scenario_d['month'] == projected_month)]['cost'].values[0]
projected_mean_e = scenario_e.loc[(scenario_e['year'] == year) & (scenario_e['month'] == projected_month)]['cost'].values[0]

estimated_mean = means_per_month[projected_month]

"""
fig, ax = plt.subplots()
ax.plot(typical_days[0], label='Día típico 2022')
ax.plot(typical_days[0]/estimated_mean * projected_mean_a, label='Escenario A')
ax.plot(typical_days[0]/estimated_mean * projected_mean_b, label='Escenario B')
ax.plot(typical_days[0]/estimated_mean * projected_mean_c, label='Escenario C')
ax.plot(typical_days[0]/estimated_mean * projected_mean_d, label='Escenario D')
ax.plot(typical_days[0]/estimated_mean * projected_mean_e, label='Escenario E')
n_month = get_month_from_number(projected_month)
plt.title(f'Proyección del costo marginal del día típico de \n {n_month} {year} de versus día típico de {n_month} de \n2022 según proyección de escenario A')
plt.xlabel('Hora')
plt.ylabel('Costo marginal $\\frac{USD}{MWh}$')
ax.legend()
plt.show()
"""

# Exporting results 
dates = []
costs_projections = []
for year in range(2024, 2045):
    for month in range(1, 13):
        projected_mean = scenario_a.loc[(scenario_a['year'] == year) & (scenario_a['month'] == month)]['cost'].values[0]
        estimated_mean = means_per_month[month - 1]
        typical_day = np.array(typical_days[month - 1])
        costs_projections += list(typical_day/estimated_mean * projected_mean)
        
        for hour in range(1, 25):
            dates.append(f'{year}-{month}-{hour}')

dates = pd.Series(dates, name='dates')
costs_projections = pd.Series(costs_projections, name='cost_predictions')



print(dates)
print(costs_projections)



#projections = pd.DataFrame(['data', ])
#print(scenario_a.cost.head())