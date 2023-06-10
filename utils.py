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