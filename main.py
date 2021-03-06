import time
from typing_test import TypingTest
from __init__ import get_configuration
import os
import json
from termcolor import colored

configuration_file_name = 'configuration.json'
configuration_file = open(configuration_file_name, 'r')
configuration_json = json.load(configuration_file)
track_progress = configuration_json['track progress']['current']



n_of_words, start_method, diffculty = get_configuration()

tt = TypingTest()

if start_method == 'enter':
    input('press enter to start:\n')
elif start_method == 'timer':
    print('Typing test will start in 5 seconds')
    index = 0
    while True:
        if index == 5:
            print('START!')
            break
        print(5 - index)
        index += 1
        time.sleep(1)

init_time = time.time()
words = tt.get_random_words()
words_str = ', '.join(words)
print('\n \n')
print(colored('========================================================================================', 'blue'))
print(words_str)
try:
    input_words = input('enter the words: \n')
except KeyboardInterrupt:
    print('\nEXIT!')
    erase = input('erase?( press enter to clean)')
    if erase == 'n':
        exit()

    os.system('cls')
    exit()
input_words_list = input_words.split(' ')

index = 0
correct_words = []
incorrect_words = []
try:
    for input_word in input_words_list:
        word = words[index]
        if word == input_word:
            correct_words.append(word)
        else:
            incorrect_words.append(word)

        index += 1
except IndexError:
    print(colored('the number of words entered are more than the number of words printed out. You probably made some mistake while typing which resulted in this. Please try again', 'red'))
#
time_taken = round(time.time() - init_time, 1)
raw_wpm, total_number_of_char = tt.calculate_wpm(words, time_taken)
raw_wpm = colored(round(raw_wpm, 1), 'cyan')
total_number_of_char = colored(total_number_of_char, 'cyan')
wpm, correct_number_of_char = tt.calculate_wpm(correct_words, time_taken)
wpm = colored(round(wpm, 1), 'cyan')
correct_words = colored(correct_words, 'cyan')
accuracy = colored(str(len(correct_words) / len(words) * 100), 'cyan')
time_taken = colored(str(round(time.time() - init_time, 1)), 'cyan')

print(colored('========================================================================================', 'blue'))
print('\n \n')
space = '                         '
print(f'{space}Accuracy = {accuracy}%\n')
print(f'{space}time taken = {time_taken}\n')
print(f'{space}Raw wpm: {raw_wpm}\n')
print(f'{space}wpm = {wpm}\n')
incorrect_words_str = ', '.join(incorrect_words)
print(f'{space}incorrect words: {incorrect_words_str}\n')
print(f'{space}correct number of characters: {correct_number_of_char}\n')
print(f'{space}total number of characters: {total_number_of_char}\n')

if track_progress == True:
    from track_practice import TrackPractice
    from datetime import date, datetime

    today = date.today()
    todays_date = today.strftime("%d/%m/%Y")
    
    curr_time = datetime.now().strftime("%H:%M:%S")
    practice_tracker = TrackPractice('progress.hdn')
    practice_tracker.enter_typing_data(time_taken, raw_wpm, wpm, accuracy, todays_date, curr_time)

erase = input('erase?( press enter to clean) redo? (press "r")')
if erase == 'n':
    exit()
elif erase == 'r':
    os.system('python3 main.py')

os.system('cls')
