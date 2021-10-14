with open('dictionary.txt', 'r') as f:
    words = f.read().split(',')

first_100_words = []
words_100_str = ''
index = 0
for word in words:
    word_with_comma = word + ','
    words_100_str += word_with_comma
    if index == 100:
        break
    index += 1

# words_100_str = ','.join(first_100_words)
with open('easy_difficulty', 'w') as f:
    f.write(words_100_str)