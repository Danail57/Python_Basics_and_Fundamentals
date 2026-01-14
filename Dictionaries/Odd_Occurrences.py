sequence_of_words = input().split(" ")
dictionary = {}

for word in sequence_of_words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
