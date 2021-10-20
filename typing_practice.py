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
        os.system('python3 configure.py')
    elif platform == 'win32':
        os.system('py configure.py')
elif command == 'release_notes':
    os.chdir('typing_practice')
    if platform == 'linux':
        os.system('xdg-open release_notes.html')
    elif platform == 'win32':
        os.system('start release_notes.html')
elif command == 'sentence':
    os.chdir('typing_practice')
    file = 'all_letters_sentence.py'
    if platform == 'linux':
        os.system(f'python3 {file}')
    elif platform == 'win32':
        os.system(f'py {file}')

elif command == 'show' and sys.argv[2] == 'progress':
    os.chdir('typing_practice')
    file = 'track_practice.py'
    if platform == 'linux':
        os.system(f'python3 {file} show_progress')
    elif platform == 'win32':
        os.system(f'py {file} show_progress')