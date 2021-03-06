import json


# configuration_json = json.load(configuration_file)
    
def get_configuration():
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'r')
    configuration_json = json.load(configuration_file)
    
    n_of_words = configuration_json['no. of words']['current']
    
    start_method = configuration_json['start method']['current']
    difficulty = configuration_json['difficulty']['current']
    track_progress = configuration_json['track progress']['current']
    return n_of_words, start_method, difficulty, track_progress

what_to_configure = input('what to configure? (type help to get more information): ')
n_of_words, start_method, difficulty, track_progress = get_configuration()

def set_config(n_of_words=n_of_words, start_method=start_method, difficulty= difficulty, track_progress=track_progress):
    # n_of_words, start_method, difficulty, track_progress = get_configuration()
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'w')
    new_config = {
        "no. of words" : {
        "current" : n_of_words,
        "options" : "however many you want"
        },
        "start method" : {
            "current" : start_method,
            "seconds" : None,
            "options" : ["enter", "timer"]
        },
        "difficulty" : {
            "current" : difficulty,
            "options" : ["easy", "difficult"]
        },
        "track progress" : {
            "current" : track_progress,
            "options" : [True, False]
        }
    }
    json.dump(new_config, configuration_file, indent=4)


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
    set_config(start_method=method)

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
    set_config(n_of_words=new_no_of_words)

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
    set_config(difficulty=new_diffculty)

elif what_to_configure == '!show config':
    configuration_file_name = 'configuration.json'
    configuration_file = open(configuration_file_name, 'r')
    configuration_json = json.load(configuration_file)
    print('\n\n')
    for obj in configuration_json:
        # print(type(obj))
        if obj != 'version':
            current = configuration_json[obj]['current']
            options = configuration_json[obj]['options']
            print(f'| {obj} | current: {current}| options: {options}')

elif what_to_configure == 'track progress':
    new_track_progress = input('do you want to track your progress?(y/N): ')
    if new_track_progress == 'y':
        track_progress = True
    elif new_track_progress == 'N':
        track_progress = False
    else:
        print('Abort!')
        exit()

    set_config(track_progress=track_progress)
    print('\n\n')
