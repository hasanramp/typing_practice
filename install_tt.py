import os
import sys
from sys import platform
import time


command = sys.argv[1]
if command == 'install':
    print('reached here')
    os.system('git clone https://github.com/hasanramp/typing_practice.git')
elif command == 'run':
    os.chdir('typing_practice')
    if platform == 'win32':
        os.system('py main.py')
    elif platform == 'linux':
        os.system('python3 main.py')
elif command == 'update':
    os.chdir('typing_practice')
    os.system('git pull')
    print('preparing to run update.py')
    time.sleep(3)
    if platform == 'linux':
        os.system('python3 update.py')
    elif platform == 'win32':
        os.system('py update.py')

elif command == 'update':
    os.system('rmdir typing_practice')
elif command == 'configure':
    os.chdir('typing_practice')
    if platform == 'linux':
        os.chdir('typing_practice')
        os.system('python3 configure.py')
    elif platform == 'win32':
        os.system('py configure.py')

