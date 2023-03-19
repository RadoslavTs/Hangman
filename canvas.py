from tkinter import Tk, Canvas


def create_root():
    root = Tk()

    root.title('Hangman')
    root.geometry('600x600')
    root.resizable(False, False)
    root.configure(bg='white')

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
