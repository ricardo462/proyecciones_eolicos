import os 
from contextlib import contextmanager
import re
import pandas as pd

@contextmanager
def cwd(path: str):
    """
    Manages the directory in order to return to the original path
    after executing the code below 'with'
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

def get_year(x):
    numbers = re.findall('\d+', x)
    return int(numbers[0])

def get_month(x):
    numbers = re.findall('\d+', x)
    return int(numbers[1])

def get_day(x):
    numbers = re.findall('\d+', x)
    return int(numbers[2])

def get_hour(x):
    numbers = re.findall('\d+', x)
    return int(numbers[3])

def to_float(x):
    numbers = x.split(',')
    return float(f'{numbers[0]}.{numbers[1]}') if len(numbers) == 2 else float(numbers[0])

def get_projected_year(x):
    x = str(x)
    data = x.split('-')
    return int(data[0])

def get_projected_month(x):
    x = str(x)
    data =x.split('-')
    #months = {'enero':1, 'febrero':2 , 'marzo':3, 'abril':4, 'mayo':5, 'junio':6,
    #          'julio':7, 'agosto':8, 'septiembre':9, 'octubre':10, 'noviembre':11, 'diciembre':12}
    #return months[int(data[1])]
    return int(data[1])

def get_scenario(path):
    scenario = pd.read_excel(path, names=['date', 'bar', 'cost'])
    scenario['year'] = scenario['date'].apply(get_projected_year)
    scenario['month'] = scenario['date'].apply(get_projected_month)
    return scenario

def get_real_costs(path):
    costs = pd.read_csv(path, names=['date', 'wrong_cost', 'cost'], skiprows=1, sep=';')
    costs['cost'] = costs['cost'].apply(to_float)
    costs.drop('wrong_cost', inplace=True, axis=1)
    costs['year'] = costs['date'].apply(get_year)
    costs['month'] = costs['date'].apply(get_month)
    costs['day'] = costs['date'].apply(get_day)
    costs['hour'] = costs['date'].apply(get_hour)
    return costs


def get_month_from_number(number):
    months = {1:'enero', 2:'febrero' , 3:'marzo', 4:'abril', 5:'mayo', 6:'junio',
              7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    return months[number]

def get_costs_projections(scenario, typical_day, estimated_mean, year, month):
    projected_mean = scenario.loc[(scenario['year'] == year) & (scenario['month'] == month)]['cost'].values[0]
    return list(typical_day/estimated_mean * projected_mean)