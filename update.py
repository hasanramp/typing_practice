from sys import platform
import os
import json

cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
print('updating installer')
if platform == 'linux':
    os.system(f'mv typing_practice.py {parent_dir}/typing_practice.py')
elif platform == 'win32':
    os.system(f'move typing_practice.py {parent_dir}/typing_practice.py')

configuration_file_name = 'configuration.json'
configuration_file = open(configuration_file_name, 'r')
configuration_json = json.load(configuration_file)


if configuration_json['version'] == "1.0.0":
    print('opening release notes')
    os.chdir(parent_dir)
    if platform == 'linux':
        os.system('python3 typing_practice.py release notes')
    elif platform == 'win32':
        os.system('py install_tt.py release notes')