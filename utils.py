import os 
from contextlib import contextmanager
import re

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