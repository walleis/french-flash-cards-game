from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

def next_card():
    '''Generate random word in the program and shows them after 3 seconds.'''
    global current_card, flip_timer
    window.after_cancel(flip_timer) # Cancel the flip_timer.
    current_card = random.choice(to_learn) # Choose a random card.
    canvas.itemconfig(card_background, image=card_front_img) # Changes the canvas features.
    canvas.itemconfig(card_title, text="French", fill="black") # Changes the canvas features.
    canvas.itemconfig(card_word, text=current_card["French"], fill="black") # Changes the canvas features.
    flip_timer = window.after(3000, flip_card)  # After 3 seconds this code flip the card.

def flip_card():
    '''It changes the actual word to the english translation and the card background.'''
    canvas.itemconfig(card_background, image=card_back_image) # Changes the canvas features.
    canvas.itemconfig(card_title, text="English", fill="white") # Changes the canvas features.
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") # Changes the canvas features.

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# Data
try:
    words_data = pandas.read_csv(filepath_or_buffer= "./data/words_to_learn.csv") # Read the .csv data.
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")  # Transforms the words data into a Python dictionary.

# Window features
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="./images/card_front.png") # Card front image.
card_background = canvas.create_image(400, 263, image=card_front_img) # Card front image item.
card_back_image = PhotoImage(file="./images/card_back.png") # Card back image.

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic")) # Card title.
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold")) # Card word.
canvas.grid(column=0, row= 0, columnspan=2)

# Buttons
right_button_image = PhotoImage(file="./images/right.png") # Right button image.
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png") # Wrong button image.
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, flip_card) # After 3 seconds this code flip the card.
next_card() # Starts the program with a card already.

# Keeps the window open.
window.mainloop()