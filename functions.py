from canvas import frame
import random


def clean_screen():
    frame.delete('all')


def guess_letter(letter, words_in, dash):
    if letter == words_in:
        return letter
    if letter in words_in:
        for i in range(len(words_in)):
            if words_in[i] == letter:
                dash[i] = letter
        return dash
    else:
        return False


word_list = []

with open('db/words.txt', 'r') as file:
    for line in file:
        word_list.append(line[:-1])


def get_word():
    return random.choice(word_list)