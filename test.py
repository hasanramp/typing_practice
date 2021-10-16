import os
from sys import platform

cwd = os.getcwd()

parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
