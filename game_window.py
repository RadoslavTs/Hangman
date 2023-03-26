import tkinter
from tkinter import Button, Entry, Label
from canvas import root, frame
from functions import guess_letter, get_word, clean_screen, dashes_draw
from PIL import ImageTk
from PIL import Image


# Function to disable buttons if already used
def button_disabling(input_letter=None):
    if input_letter:
        for button in buttons:
            if input_letter == button['text']:
                button.config(state='disabled', relief='groove')
                break
    else:
        for button in buttons:
            for i in range(len(dashes)):
                if button['text'] == dashes[i]:
                    button.config(state='disabled', relief='groove')


# Function to render the main screen of the game
def render_main():
    frame.create_text(325, 50, text='Classic Hangman!', font=('Comic Sans MS', 30))
    frame.create_window(600, 640, window=replay_button)
    frame.create_window(300, 450, window=label_word)
    frame.create_window(500, 450, window=remaining_lives_label)
    frame.create_window(200, 450, window=result_label)
    frame.create_window(350, 270, window=image_label)

    # Keyboard
    x, y = 125, 500
    x_row_two = 160
    x_row_three = 195
    step_x, step_y = 50, 70
    # Row 1
    frame.create_window(x, y, window=button_q)
    frame.create_window(x+step_x, y, window=button_w)
    frame.create_window(x+step_x*2, y, window=button_e)
    frame.create_window(x+step_x*3, y, window=button_r)
    frame.create_window(x+step_x*4, y, window=button_t)
    frame.create_window(x+step_x*5, y, window=button_y)
    frame.create_window(x+step_x*6, y, window=button_u)
    frame.create_window(x+step_x*7, y, window=button_i)
    frame.create_window(x+step_x*8, y, window=button_o)
    frame.create_window(x+step_x*9, y, window=button_p)
    # Row 2
    frame.create_window(x_row_two, y+step_y, window=button_a)
    frame.create_window(x_row_two+step_x, y+step_y, window=button_s)
    frame.create_window(x_row_two+step_x*2, y+step_y, window=button_d)
    frame.create_window(x_row_two+step_x*3, y+step_y, window=button_f)
    frame.create_window(x_row_two+step_x*4, y+step_y, window=button_g)
    frame.create_window(x_row_two+step_x*5, y+step_y, window=button_h)
    frame.create_window(x_row_two+step_x*6, y+step_y, window=button_j)
    frame.create_window(x_row_two+step_x*7, y+step_y, window=button_k)
    frame.create_window(x_row_two+step_x*8, y+step_y, window=button_l)
    # Row 3
    frame.create_window(x_row_three, y+step_y*2, window=button_z)
    frame.create_window(x_row_three+step_x, y+step_y*2, window=button_x)
    frame.create_window(x_row_three+step_x*2, y+step_y*2, window=button_c)
    frame.create_window(x_row_three+step_x*3, y+step_y*2, window=button_v)
    frame.create_window(x_row_three+step_x*4, y+step_y*2, window=button_b)
    frame.create_window(x_row_three+step_x*5, y+step_y*2, window=button_n)
    frame.create_window(x_row_three+step_x*6, y+step_y*2, window=button_m)


# Function to handle the guessing
def handle_guess(letter):
    global lives_left
    global won_flag
    global label_word
    global dashes
    global false_guesses

    result = guess_letter(letter, word, dashes)
    if lives_left == 0 or won_flag:
        pass
    else:
        if result:
            label_word.config(text=' '.join(result))
            dashes = result
            if '_' not in result:
                remaining_lives_label.config(text='YOU WON!', fg='green')
                won_flag = True

        else:
            lives_left -= 1
            remaining_lives_label.config(text=f'Remaining lives: {lives_left}')
            false_guesses.append(letter)
            button_disabling(letter)
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
                image_label.config(image=dead_image)
    button_disabling()


# Function to handle the new game button
def new_game():
    global lives_left
    global word
    global dashes
    global remaining_lives_label
    global result_label
    global image_label
    global label_word
    global won_flag
    global false_guesses
    clean_screen()
    word = get_word()
    lives_left = 6
    false_guesses = []
    for letter_button in buttons:
        letter_button.config(state='normal', relief='flat')
    dashes = dashes_draw(word)
    label_word.config(text=' '.join(dashes))
    button_disabling()
    guess_entry.delete(0, tkinter.END)
    won_flag = False
    remaining_lives_label = Label(text=f'Remaining lives: {lives_left}')
    result_label = Label(text='Result')
    image_label = tkinter.Label(image=full_hp_image)
    label_word = Label(text=' '.join(dashes))

    render_main()


# Images loading
full_hp_image = ImageTk.PhotoImage(Image.open('images/full_hp.jpg'))
dead_image = ImageTk.PhotoImage(Image.open('images/dead.jpg'))
one_hp_image = ImageTk.PhotoImage(Image.open('images/1_hp.jpg'))
two_hp_image = ImageTk.PhotoImage(Image.open('images/2_hp.jpg'))
three_hp_image = ImageTk.PhotoImage(Image.open('images/3_hp.jpg'))
four_hp_image = ImageTk.PhotoImage(Image.open('images/4_hp.jpg'))
five_hp_image = ImageTk.PhotoImage(Image.open('images/5_hp.jpg'))

# keyboard buttons creation
button_a = Button(root, text='a', font=('Arial', 20), width=2, command=lambda x='a': handle_guess(x))
button_b = Button(root, text='b', font=('Arial', 20), width=2, command=lambda x='b': handle_guess(x))
button_c = Button(root, text='c', font=('Arial', 20), width=2, command=lambda x='c': handle_guess(x))
button_d = Button(root, text='d', font=('Arial', 20), width=2, command=lambda x='d': handle_guess(x))
button_e = Button(root, text='e', font=('Arial', 20), width=2, command=lambda x='e': handle_guess(x))
button_f = Button(root, text='f', font=('Arial', 20), width=2, command=lambda x='f': handle_guess(x))
button_g = Button(root, text='g', font=('Arial', 20), width=2, command=lambda x='g': handle_guess(x))
button_h = Button(root, text='h', font=('Arial', 20), width=2, command=lambda x='h': handle_guess(x))
button_i = Button(root, text='i', font=('Arial', 20), width=2, command=lambda x='i': handle_guess(x))
button_j = Button(root, text='j', font=('Arial', 20), width=2, command=lambda x='j': handle_guess(x))
button_k = Button(root, text='k', font=('Arial', 20), width=2, command=lambda x='k': handle_guess(x))
button_l = Button(root, text='l', font=('Arial', 20), width=2, command=lambda x='l': handle_guess(x))
button_m = Button(root, text='m', font=('Arial', 20), width=2, command=lambda x='m': handle_guess(x))
button_n = Button(root, text='n', font=('Arial', 20), width=2, command=lambda x='n': handle_guess(x))
button_o = Button(root, text='o', font=('Arial', 20), width=2, command=lambda x='o': handle_guess(x))
button_p = Button(root, text='p', font=('Arial', 20), width=2, command=lambda x='p': handle_guess(x))
button_q = Button(root, text='q', font=('Arial', 20), width=2, command=lambda x='q': handle_guess(x))
button_r = Button(root, text='r', font=('Arial', 20), width=2, command=lambda x='r': handle_guess(x))
button_s = Button(root, text='s', font=('Arial', 20), width=2, command=lambda x='s': handle_guess(x))
button_t = Button(root, text='t', font=('Arial', 20), width=2, command=lambda x='t': handle_guess(x))
button_u = Button(root, text='u', font=('Arial', 20), width=2, command=lambda x='u': handle_guess(x))
button_v = Button(root, text='v', font=('Arial', 20), width=2, command=lambda x='v': handle_guess(x))
button_w = Button(root, text='w', font=('Arial', 20), width=2, command=lambda x='w': handle_guess(x))
button_x = Button(root, text='x', font=('Arial', 20), width=2, command=lambda x='x': handle_guess(x))
button_y = Button(root, text='y', font=('Arial', 20), width=2, command=lambda x='y': handle_guess(x))
button_z = Button(root, text='z', font=('Arial', 20), width=2, command=lambda x='z': handle_guess(x))


# Variables
buttons = [button_a, button_b, button_c, button_d, button_e, button_f, button_g, button_h, button_i,
           button_j, button_k, button_l, button_m, button_n, button_o, button_p, button_q, button_r,
           button_s, button_t, button_u, button_v, button_w, button_x, button_y, button_z]

false_guesses = []
lives_left = 6
won_flag = False
remaining_lives_label = Label(text=f'Remaining lives: {lives_left}')
replay_button = Button(root, text='Play new game', bg='green', fg='white', borderwidth=0, width=20, height=3, command=new_game,)
result_label = Label(text='Result')
image_label = tkinter.Label(image=full_hp_image)
word = get_word()
dashes = dashes_draw(word)
button_disabling()
label_word = Label(text=' '.join(dashes))
guess_entry = Entry(root, bd=0)
