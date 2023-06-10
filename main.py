from utils import cwd
import os
import pandas as pd

PATH = 'data'

with cwd(PATH):
    files = os.listdir()
    esc_a = pd.read_excel(files[0])

print(esc_a.head)
    
