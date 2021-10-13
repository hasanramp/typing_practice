import json
from __init__ import get_configuration


# configuration_json = json.load(configuration_file)
    

what_to_configure = input('what to configure? (type help to get more information): ')

if what_to_configure == 'start method':
    method = input('new start method: ')
    n_of_words, start_method = get_configuration()
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
        }
    }
    json.dump(new_config, configuration_file, indent=4)

elif what_to_configure == 'no of words':
    new_no_of_words = int(input('new number of words: '))
    n_of_words, start_method = get_configuration()
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
        }
    }
    json.dump(new_config, configuration_file, indent=4)
