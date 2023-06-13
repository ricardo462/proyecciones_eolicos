from utils import cwd
import os
import numpy as np
import pandas as pd

DATA_PATH = 'data'
FILE_NAME = 'Generacion_aerogeneradores_2024-2043.xlsx'
PROJECTIONS_FILE_NAME = 'proyecciones.xlsx'


days_per_month = 365 / 12
scenario = 'escenario_a'
sheets_names = ['Aerogeneradores', 'Goldwind GW87 1500', 'Vestas V110 2000', 'Vestas V100 2000']
columns_names = ['year', 'month', 'hora', 'wind_speed', 'rounded_wind_speed',
                  'potencia_aerogenerador_k', 'potencia_aerogenerador_m', 'energia_aerogenerador', 'energia_total']

with cwd(DATA_PATH):
    generacion = pd.read_excel(FILE_NAME, sheet_name=sheets_names[1], usecols='A:I', names=columns_names)
    generacion.reset_index(inplace=True, drop=True)
    projections = pd.read_excel(PROJECTIONS_FILE_NAME)
    generacion = generacion.drop([i for i in range(8)])





scenario = projections[scenario].apply(pd.to_numeric)
energy = generacion['energia_total'].apply(pd.to_numeric)
energy.reset_index(inplace=True, drop=True)
money = scenario*energy
result = pd.DataFrame()
result['year'] = generacion['year'].reset_index(drop=True)
result['month'] = generacion['month'].reset_index(drop=True)
result['hora'] = generacion['hora'].reset_index(drop=True)
result['scenario'] = scenario
result['energy'] = energy
result['money'] = money
result.reset_index(inplace=True, drop=True)


money_per_months = []
money_per_years = []
for year in range(2024, 2044):
    money_per_year = []
    for month in ['enero', 'febrero' , 'marzo', 'abril', 'mayo', 'junio','julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']:
        money_per_typical_day = result.loc[(result['year'] == year) & (result['month'] == month)]['money'].values
        money_per_month = (money_per_typical_day * days_per_month).sum()
        money_per_months.append(money_per_month)
        money_per_year.append(money_per_month)

    money_per_year = np.array(money_per_year)
    money_per_year = money_per_year.sum()
    money_per_years.append(money_per_year)

money_per_months = np.array(money_per_months)
money_per_years = np.array(money_per_years)
print(money_per_months.shape, money_per_months.sum())
print(money_per_years.shape, money_per_years.sum())