import random
from csv import reader
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# Apply words from csv to card
word_file = pd.read_csv("data/french_words.csv")
words = word_file.to_dict(orient="records")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    words.remove(current_card)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

# Create canvas for cards
canvas = Canvas(width=800, height=600,
                bg=BACKGROUND_COLOR, highlightthickness=0)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
card_background = canvas.create_image(400, 300, image=card_front)


card_title = canvas.create_text(
    400, 150, text="French", font=("Arial", 20, "italic"))
card_word = canvas.create_text(
    400, 300, text="Word", font=("Arial", 60, "italic"))


canvas.grid(row=0, column=0, columnspan=2)

right_button = Button(image=right, highlightthickness=0,
                      bg=BACKGROUND_COLOR, command=new_card)
wrong_button = Button(image=wrong, highlightthickness=0,
                      bg=BACKGROUND_COLOR, command=flip_card)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

new_card()

window.mainloop()
