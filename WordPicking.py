import random


def word_pick():

    words_file = open("words.txt", "r")
    words = [line.rstrip() for line in words_file]
    word_picking = random.choice(words)

    return word_picking

print(word_pick())


