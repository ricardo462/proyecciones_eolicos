import os 
from contextlib import contextmanager

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