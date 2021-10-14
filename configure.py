import json
from __init__ import get_configuration


# configuration_json = json.load(configuration_file)
    

what_to_configure = input('what to configure? (type help to get more information): ')

def get_options(setting):
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'r')
    configuration_json = json.load(configuration_file)
    return configuration_json[setting]['options']


if what_to_configure == 'start method':
    method = input('new start method: ')
    if method == '!options':
        options = get_options('start method')
        options_str = ''
        for option in options:
            option_with_comma = option + ','
            options_str += option_with_comma
        
        print('options are: ' + options_str)
        exit()
    n_of_words, start_method, difficulty = get_configuration()
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'w')
    new_config = {
        "no. of words" : {
        "current" : n_of_words
        },
        "start method" : {
            "current" : method,
            "seconds" : None,
            "options" : ["enter", "timer"]
        },
        "difficulty" : {
        "current" : difficulty,
        "options" : ["easy", "difficult"]
        }
    }
    json.dump(new_config, configuration_file, indent=4)

elif what_to_configure == 'no of words':
    new_no_of_words = input('new number of words: ')
    if new_no_of_words == '!options':
        options = get_options('no. of words')
        options_str = ''
        for option in options:
            option_with_comma = option + ','
            options_str += option_with_comma
        print('options are: ' + options_str)
        exit()
    else:
        new_no_of_words = int(new_no_of_words)
    n_of_words, start_method, difficulty = get_configuration()
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'w')
    new_config = {
        "no. of words" : {
        "current" : new_no_of_words
        },
        "start method" : {
            "current" : start_method,
            "seconds" : None,
            "options" : ["enter", "timer"]
        },
        "difficulty" : {
        "current" : difficulty,
        "options" : ["easy", "difficult"]
        }
    }
    json.dump(new_config, configuration_file, indent=4)

elif what_to_configure == 'difficulty':
    new_diffculty = input('new difficulty: ')
    if new_diffculty == '!options':
        options = get_options('difficulty')
        options_str = ''
        for option in options:
            option_with_comma = option + ','
            options_str += option_with_comma
        print('options are: ' + options_str)
        exit()
    n_of_words, start_method, difficulty = get_configuration()
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'w')
    new_config = {
        "no. of words" : {
        "current" : n_of_words
        },
        "start method" : {
            "current" : start_method,
            "seconds" : None,
            "options" : ["enter", "timer"]
        },
        "difficulty" : {
        "current" : new_diffculty,
        "options" : ["easy", "difficult"]
        }
    }
    json.dump(new_config, configuration_file, indent=4)