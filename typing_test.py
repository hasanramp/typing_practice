import random2
from __init__ import get_configuration
from sys import platform
class TypingTest:
    def __init__(self):
        self.random_no_of_words, self.start_method, self.difficulty = get_configuration()

    def get_random_words(self):
        if self.difficulty == 'easy':
            with open('easy_difficulty.txt', 'r') as f:
                words_list = f.read().split(',')
        elif self.difficulty == 'difficulty':
            with open('dictionary.txt', 'r') as f:
                words_list = f.read().split(',')
        else:
            if platform == 'linux':
                file = 'typing_practice.py'
                python_interpreter_call_command = 'python3'
            elif platform == 'win32':
                file = 'install_tt.py'
                python_interpreter_call_command = 'py'
            else:
                print('this app is not supported for macOS. Kuhahahahahaha. Apple suuuuuucks!!!')
                exit()
            print(f'There was some mistake in the difficulty in configuration file. Use "{python_interpreter_call_command} {file} configure" to fix this issue')
            print('The difficulty options are: easy & difficult. Enter one of these when prompted.')
        random_words = []
        for x in range(0 , self.random_no_of_words):
            random_word = random2.choice(words_list)
            random_words.append(random_word)
        
        return random_words
    
    def calculate_wpm(self, words, time_taken):
        number_of_characters = 0
        for word in words:
            number_of_characters += len(word)
        
        number_of_characters = number_of_characters + len(words) - 1
        average_number_of_words = number_of_characters / 5
        wpm = average_number_of_words / (time_taken / 60), number_of_characters
        return wpm

if __name__ == '__main__':    
    tt = TypingTest()
    print(tt.get_random_words(25))
    