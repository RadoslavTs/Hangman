from tkinter import Tk, Canvas


# Function to create the main root of the game
def create_root():
    root = Tk()

    root.title('Hangman')
    root.geometry(f'{700}x{750}')
    root.resizable(False, False)
    root.configure(bg='#F0F0F0')
    root.iconbitmap('images/hangman_icon.ico')

    return root


# Function that return a frame
def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
