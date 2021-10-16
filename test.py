import os
from sys import platform

cwd = os.getcwd()
if platform == 'linux':
    print(os.path.abspath(os.path.join(cwd, os.pardir)))
