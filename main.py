import time
import random2
from typing_test import TypingTest

tt = TypingTest()

input('press enter to start: ')
init_time = time.time()
words = tt.get_random_words(50)
words_str = ', '.join(words)
print('\n \n')
print('========================================================================================')
print(words_str)
input_words = input('enter the words: ')
input_words_list = input_words.split(' ')

index = 0
correct_words = []
incorrect_words = []
for input_word in input_words_list:
    word = words[index]
    if word == input_word:
        correct_words.append(word)
    else:
        incorrect_words.append(word)

    index += 1

time_taken = round(time.time() - init_time, 1)
raw_wpm, total_number_of_char = tt.calculate_wpm(words, time_taken)
wpm, correct_number_of_char = tt.calculate_wpm(correct_words, time_taken)
accuracy = len(correct_words) / len(words) * 100

print('========================================================================================')
print('\n \n')
print(f'Accuracy = {accuracy}%\n')
print(f'time taken = {time_taken}\n')
print(f'Raw wpm: {raw_wpm}\n')
print(f'wpm = {wpm}\n')
incorrect_words_str = ', '.join(incorrect_words)
print(f'incorrect words: {incorrect_words_str}\n')
print(f'correct number of characters: {correct_number_of_char}\n')
print(f'total number of characters: {total_number_of_char}\n')
