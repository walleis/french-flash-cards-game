# Flash Cards - French to English

## Description

This Python application is a flash card program designed to help users learn French vocabulary. It presents a French word on a card and automatically flips the card after 3 seconds to reveal its English translation. Users can indicate whether they knew the word or not, which helps the program track words that need more practice. The application saves the words the user still needs to learn in a separate CSV file for future sessions.

## How to Use

1.  **Run the script:** Execute the Python script. A window titled "Flash Cards" will appear with a French word displayed on a card.
2.  **View the French word:** The French word will be shown on the front of the card.
3.  **Automatic Flip:** After 3 seconds, the card will automatically flip to reveal the English translation of the word.
4.  **Indicate Knowledge:**
    * **Right Button (✔):** If you knew the French word, click the green "right" button. This will remove the current word from the learning list and display the next French word. The program will also update a CSV file (`words_to_learn.csv`) to exclude this word in future sessions.
    * **Wrong Button (❌):** If you did not know the French word, click the red "wrong" button. This will keep the current word in the learning list and display the next French word.
5.  **Continue Learning:** The program will continue to present French words and their English translations until you have gone through all the words or close the application.
6.  **Saving Progress:** The program attempts to load words you still need to learn from `./data/words_to_learn.csv`. If this file doesn't exist, it loads all French words from `./data/french_words.csv`. When you click the "right" button (indicating you know a word), the `words_to_learn.csv` file is updated to exclude that word for subsequent sessions.

## Functionality

* **French to English Flashcards:** Presents French words and their English translations.
* **Automatic Card Flip:** Automatically flips the card after a 3-second delay.
* **"Known" and "Unknown" Buttons:** Allows users to indicate whether they knew the word.
* **Word Tracking:** Keeps track of words the user indicates they don't know.
* **Data Persistence:** Saves the list of words to learn in a CSV file (`words_to_learn.csv`) to maintain learning progress across sessions.
* **Initial Data Loading:** Loads French words and their English translations from `./data/french_words.csv`.
* **GUI Interface:** Uses Tkinter to create a user-friendly interface with a card display and buttons.

## Requirements

* Python 3.x
* `tkinter` module (typically included with standard Python installations)
* `random` module (built-in)
* `pandas` library (can be installed via pip: `pip install pandas`)
* Image files in a directory named `./images/`:
    * `card_front.png`: Image for the front of the flash card.
    * `card_back.png`: Image for the back of the flash card.
    * `right.png`: Image for the "known" button.
    * `wrong.png`: Image for the "unknown" button.
* Data files in a directory named `./data/`:
    * `french_words.csv`: A CSV file containing French words and their English translations. It should have columns named "French" and "English".
    * `words_to_learn.csv` (optional): This file will be created and updated by the program to store the words the user still needs to learn.

## Installation

1.  Ensure you have Python installed on your system.
2.  Install the `pandas` library if it's not already installed:
    ```bash
    pip install pandas
    ```
3.  Create two directories named `images` and `data` in the same directory where you will save the Python script.
4.  Download the `card_front.png`, `card_back.png`, `right.png`, and `wrong.png` image files and place them in the `./images/` directory.
5.  Save the provided code as a `.py` file (e.g., `flash_cards_game.py`).
6.  Run the script using a Python interpreter:
    ```bash
    python flash_cards_game.py
    ```

## Code Explanation

* **Import Statements:** Imports necessary modules (`tkinter` for GUI, `random` for choosing random words, `pandas` for data handling).
* **Constants:** Defines the background color (`BACKGROUND_COLOR`).
* **Global Variables:**
    * `current_card`: A dictionary to store the currently displayed French and English words.
    * `to_learn`: A list of dictionaries, where each dictionary represents a word pair to learn.
    * `flip_timer`: Stores the ID of the scheduled `flip_card` function.
* **`next_card()` Function:**
    * Cancels any existing `flip_timer` to avoid multiple flips.
    * Randomly selects a word pair from the `to_learn` list and updates the `current_card`.
    * Updates the canvas to display the front of the card (French word) with black text.
    * Schedules the `flip_card()` function to be called after 3000 milliseconds (3 seconds).
* **`flip_card()` Function:**
    * Updates the canvas to display the back of the card (English translation) with white text.
* **`is_known()` Function:**
    * Removes the `current_card` from the `to_learn` list.
    * Creates a new pandas DataFrame from the updated `to_learn` list.
    * Saves the updated list of words to learn in `./data/words_to_learn.csv`, overwriting the file without the index.
    * Calls `next_card()` to display the next French word.
* **Data Loading:**
    * Uses a `try-except` block to attempt to load words to learn from `./data/words_to_learn.csv`.
    * If `FileNotFoundError` occurs (i.e., the user is running the program for the first time or hasn't marked any words as known), it loads all words from `./data/french_words.csv`.
    * In both cases, the data is converted into a list of dictionaries (`to_learn`) where each dictionary has "French" and "English" keys.
* **Window Setup:**
    * Creates the main window (`window = Tk()`).
    * Sets the window title.
    * Configures padding and background color.
* **Canvas Setup:**
    * Creates a `Canvas` widget with specified dimensions and background color, and removes the highlight border.
    * Loads the front and back card images using `PhotoImage()`.
    * Creates image items on the canvas for the front and back of the card.
    * Creates text items on the canvas to display the French word (initially empty) and its English translation (initially empty) with specified fonts and initial colors.
    * Places the canvas in the grid layout.
* **Buttons:**
    * Loads the "right" (known) and "wrong" (unknown) button images.
    * Creates `Button` widgets using these images, removes the highlight border, and assigns the `is_known()` and `next_card()` functions to their respective `command` attributes.
    * Places the buttons in the grid layout.
* **Initial Flip Timer and Card:** Schedules the initial card flip after 3 seconds and calls `next_card()` to display the first word.
* **`window.mainloop()`:** Starts the Tkinter event loop to keep the window open and interactive.
