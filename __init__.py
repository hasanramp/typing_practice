import json

def get_configuration():
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'r')
    configuration_json = json.load(configuration_file)
    
    n_of_words = configuration_json['no. of words']['current']
    
    start_method = configuration_json['start method']['current']
    difficulty = configuration_json['difficulty']['current']
    return n_of_words, start_method, difficulty
