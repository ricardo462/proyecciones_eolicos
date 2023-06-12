from utils import cwd
import os
import pandas as pd

DATA_PATH = 'data'
FILE_NAME = 'Generacion_aerogeneradores_2024-2043.xlsx'
PROJECTIONS_FILE_NAME = 'proyecciones.xlsx'

scenario = 'escenario_a'
sheets_names = ['Aerogeneradores', 'Goldwind GW87 1500', 'Vestas V110 2000', 'Vestas V100 2000']
columns_names = ['year', 'mes', 'hora', 'wind_speed', 'rounded_wind_speed',
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
result['mes'] = generacion['mes'].reset_index(drop=True)
result['hora'] = generacion['hora'].reset_index(drop=True)
result['scenario'] = scenario
result['energy'] = energy
result['money'] = money
result.reset_index(inplace=True, drop=True)




