import tkinter
from tkinter import Tk, Button, Entry, Label
from canvas import root, frame
from functions import guess_letter, get_word, clean_screen
from PIL import ImageTk
from PIL import Image


def render_main():
    frame.create_text(325, 50, text='Classic Hangman!', font=('Comic Sans MS', 30))

    frame.create_window(300, 550, window=guess_button)  # Ready
    frame.create_window(500, 550, window=replay_button)  # Ready

    frame.create_window(300, 450, window=label_word)
    frame.create_window(500, 500, window=remaining_lives_label)
    frame.create_window(300, 500, window=guess_entry)
    frame.create_text(200, 500, text='Your guess:')
    frame.create_window(200, 450, window=result_label)
    frame.create_window(325, 270, window=image_label)


def handle_guess(event=1):
    global lives_left
    global won_flag
    guess = guess_entry.get().lower()
    guess_entry.delete(0, tkinter.END)
    result = guess_letter(guess, word, dashes)
    if lives_left == 0 or won_flag:
        pass
    else:
        if result:
            label_word.config(text=' '.join(result))
            if '_' not in result:
                remaining_lives_label.config(text='YOU WON!')
                guess_button.config(state='disabled')
                won_flag = True

        else:
            lives_left -= 1
            remaining_lives_label.config(text='Remaining lives: {}'.format(lives_left))
            if lives_left == 5:
                image_label.config(image=five_hp_image)
            elif lives_left == 4:
                image_label.config(image=four_hp_image)
            elif lives_left == 3:
                image_label.config(image=three_hp_image)
            elif lives_left == 2:
                image_label.config(image=two_hp_image)
            elif lives_left == 1:
                image_label.config(image=one_hp_image)
            if lives_left == 0:
                label_word.config(text=word)
                remaining_lives_label.config(text="YOU LOSE!", fg='red')
                guess_button.config(state='disabled')
                image_label.config(image=dead_image)


def new_game():
    global lives_left
    global word
    global dashes
    global remaining_lives_label
    global result_label
    global image_label
    global label_word
    global won_flag
    clean_screen()
    word = get_word()
    lives_left = 6
    dashes = ['_'] * len(word)
    guess_entry.delete(0, tkinter.END)
    won_flag = False
    remaining_lives_label = Label(text='Remaining lives: {}'.format(lives_left))
    result_label = Label(text='Result')
    image_label = tkinter.Label(image=full_hp_image)
    label_word = Label(text=' '.join(dashes))
    guess_button.config(state='normal')

    render_main()


root.bind('<Return>', handle_guess)


word = get_word()
lives_left = 6
dashes = ['_'] * len(word)
remaining_lives_label = Label(text='Remaining lives: {}'.format(lives_left))
result_label = Label(text='Result')
won_flag = False

guess_button = Button(
    root,
    text='Take a guess',
    bg='blue',
    fg='white',
    borderwidth=0,
    width=20,
    height=3,
    command=handle_guess,
)

replay_button = Button(
    root,
    text='Play new game',
    bg='green',
    fg='white',
    borderwidth=0,
    width=20,
    height=3,
    command=new_game,
)


full_hp_image = ImageTk.PhotoImage(Image.open('images/full_hp.png'))
dead_image = ImageTk.PhotoImage(Image.open('images/dead.jpg'))
one_hp_image = ImageTk.PhotoImage(Image.open('images/1_hp.jpg'))
two_hp_image = ImageTk.PhotoImage(Image.open('images/2_hp.jpg'))
three_hp_image = ImageTk.PhotoImage(Image.open('images/3_hp.jpg'))
four_hp_image = ImageTk.PhotoImage(Image.open('images/4_hp.jpg'))
five_hp_image = ImageTk.PhotoImage(Image.open('images/5_hp.jpg'))

image_label = tkinter.Label(image=full_hp_image)

guess_button.config(command=handle_guess)
label_word = Label(text=' '.join(dashes))
guess_entry = Entry(root, bd=0)
