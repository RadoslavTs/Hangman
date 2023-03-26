from canvas import frame
import random


# Function to help clean the screen
def clean_screen():
    frame.delete('all')


# Function to check for the guessed letter
def guess_letter(letter, words_in, dash):
    dash_list = list(dash)
    if letter in words_in:
        for i in range(len(words_in)):
            if words_in[i] == letter and letter not in dash:
                dash_list[i] = letter
        dash = ''.join(dash_list)
        return dash
    else:
        return False


# Loading the database with words
word_list = []
with open('db/words.txt', 'r') as file:
    for line in file:
        word_list.append(line[:-1])


# Function to pick a random word
def get_word():
    return random.choice(word_list)


# Function to draw the necessary dashes
def dashes_draw(word):
    first_letter = word[0]
    last_letter = word[-1]
    result = ''
    for i in range(len(word)):
        if i == 0:
            result = first_letter
        elif i == len(word)-1:
            result += last_letter
        else:
            result += '_'

    return result
