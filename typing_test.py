import random2

class TypingTest:
    def __init__(self):
        pass

    def get_random_words(self, random_no_of_words):
        with open('dictionary.txt', 'r') as f:
            words_list = f.read().split(',')
        random_words = []
        for x in range(0 , random_no_of_words):
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
    