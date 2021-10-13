import time
import random2
from typing_test import TypingTest
from __init__ import get_configuration

n_of_words, start_method = get_configuration()

tt = TypingTest()

if start_method == 'enter':
    input('press enter to start: ')
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
print('========================================================================================')
print(words_str)
input_words = input('enter the words: ')
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
    print('the number of words entered are more than the number of words printed out. You probably made some mistake while typing which resulted in this. Please try again')

time_taken = round(time.time() - init_time, 1)
raw_wpm, total_number_of_char = tt.calculate_wpm(words, time_taken)
wpm, correct_number_of_char = tt.calculate_wpm(correct_words, time_taken)
accuracy = len(correct_words) / len(words) * 100

print('========================================================================================')
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
