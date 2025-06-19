import string

text = input("Text: ")

translator = str.maketrans('', '', string.punctuation)
words = text.lower().translate(translator).split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

words_sorted = sorted(word_count.keys())
max_length = max(len(word) for word in words_sorted)
print("Word Occurrences:")