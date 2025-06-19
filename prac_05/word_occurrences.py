import string

text = input("Text: ")

translator = str.maketrans('', '', string.punctuation)
words = text.lower().translate(translator).split()

word_count = {}
