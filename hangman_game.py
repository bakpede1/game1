from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import random


"""
HANGMAN GAME
---------------------

GAME DESCRIPTION:

Objective: Guess the secret word within a limited number of attempts.

Rules:
- The player has a limited number of guesses to correctly guess the letters in the secret word.
- For each incorrect guess, a part of the hangman's body is added.
- If the hangman's body is complete before the word is guessed, the player loses.
- If the player correctly guesses all the letters in the word before the hangman is complete, the player wins.

Inputs:
- The player can input a single letter as a guess using the keyboard and ENTER key.
- Mouse inputs are used to click buttons for starting the game, selecting word categories, and playing again.

Categories:
1. Fruits
2. Flowers
3. Places
4. Animals
5. Colors
6. Countries
7. Sports
8. Professions

"""
# global constants
CATEGORIES = ["Fruits", "Flowers", "Places", "Animals", "Colors", "Countries", "Sports", "Movies", "Professions"]
WORDS = {
  "Fruits": ["Apple", "Banana", "Orange", "Strawberry", "Mango", "Grapes", "Pineapple", "Watermelon", "Kiwi", "Peach"],
  "Flowers": ["Rose", "Tulip", "Sunflower", "Lily", "Daisy", "Orchid", "Carnation", "Daffodil", "Hibiscus", "Peony"],
  "Places": ["Paris", "New York", "Tokyo", "Rome", "London", "Sydney", "Barcelona", "Cairo", "Rio de Janeiro", "Amsterdam"],
  "Animals": ["Elephant", "Tiger", "Giraffe", "Lion", "Monkey", "Kangaroo", "Penguin", "Horse", "Dolphin", "Koala"],
  "Colors": ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Brown"],
  "Countries": ["United States", "China", "Russia", "India", "Brazil", "Australia", "Canada", "Mexico", "France", "Germany"],
  "Sports": ["Football", "Basketball", "Tennis", "Soccer", "Golf", "Cricket", "Baseball", "Volleyball", "Hockey", "Swimming"],
  "Professions": ["Doctor", "Teacher", "Engineer", "Lawyer", "Chef", "Artist", "Pilot", "Scientist", "Writer", "Athlete"]
}
MAX_NUM_GUESSES = 5
HANGMAN_INTRO = [
  '   ------',
  '   |    |',
  '   |    O',
  '   |   -|-',
  '   |    |',
  '   |   / \\',
  '------------'
]
HANGMAN_START = [
  '   ------',
  '   |    ',
  '   |     ',
  '   |   ',
  '   |    ',
  '   |   ',
  '------------'
]
HANGMAN_ADD = {
  0: '',
  1: '|',
  2: 'O',
  3: '-|-',
  4: '|',
  5: '/ \\',
  6: ''
}
hangman_colors= {
    "body": "black",
    "lines": "black",
    "text": "black",
}

# global screen variables
window = None
guess = None
secret = None
lives_rem = MAX_NUM_GUESSES
incorrect = None
part_of_word_guessed = None
word_label = None
lives_label = None
intro_frame = None
game_frame = None
play_again_frame = None
start = False
guess_entry = None
hm_1 = None
hm_2 = None
hm_3 = None
hm_4 = None
hm_5 = None
hm_6 = None
hm_7 = None
hangman_labels = None
last_int = 1

# helper functions
def change_body_color():
    """
    This function changes the color of the hangman's body.
    """
    global hangman_colors
    color = askcolor(color= hangman_colors["body"])[1]
    if color:
        hangman_colors["body"] = color

def change_lines_color():
    """
    This function changes the color of the hangman's lines.
    """
    global hangman_colors
    color = askcolor(color= hangman_colors["lines"])[1]
    if color:
        hangman_colors["lines"] = color

def change_text_color():
    """
    This function changes the color of the hangman's text.
    """
    global hangman_colors
  
    color = askcolor(color=hangman_colors["text"])[1]
    if color:
        hangman_colors["text"] = color


def update_hangman_colors():
    """
    This function updates the hangman labels with the new colors.
    """
    for label in hangman_labels:
        label.config(fg=hangman_colors["lines"])
    lives_label.config(fg=hangman_colors["text"])
    word_label.config(fg=hangman_colors["text"])

def config_hangman(root):
  """
  This function configures the hangman labels for displaying the hangman image.
  :param root: The parent window/frame for the hangman labels.
  """
  global hm_1, hm_2, hm_3, hm_4, hm_5, hm_6, hm_7, hangman_labels
  hangman_labels = [hm_1, hm_2, hm_3, hm_4, hm_5, hm_6, hm_7]
  for i in range(len(hangman_labels)):
    hangman_labels[i] = new_label(root,HANGMAN_START[i])
    hangman_labels[i].pack()
    hangman_labels[i].config(fg=hangman_colors["lines"])
  
def alert_msg(title, msg):
  """
  This function displays an alert message box with the given title and message.
  :param title: The title of the alert box.
  :param msg: The message to be displayed in the alert box.
  """
  messagebox.showinfo(title, msg)

def new_frame(root):
    """Creates and returns a new frame."""
    frame = Frame(root)
    return frame
  
def new_label(root=window,text=""):
  """
  This function creates and returns a new label widget.
  :param root: The parent window/frame for the label.
  :param text: The text to be displayed in the label.
  :return: The newly created label widget.
  """
  return Label(root, text=text)
  
def new_button(root=window,text="",cmd=None):
  """
  This function creates and returns a new button widget.
  :param root: The parent window/frame for the button.
  :param text: The text to be displayed on the button.
  :param cmd: The command to be executed when the button is clicked.
  :return: The newly created button widget.
  """
  if cmd is None:
    return Button(root, text=text)
  return Button(root, text=text, command=cmd)

def new_entry(root=window,font=None):
  """
  This function creates and returns a new entry widget.
  :param root: The parent window/frame for the entry.
  :param font: The font to be used for the entry text.
  :return: The newly created entry widget.
  """
  return Entry(root, font=font)
  
def clear_window():
  """
  This function clears the contents of the window by destroying all widgets.
  """
  for widget in window.winfo_children():
    widget.destroy()

def play_again():
  """
  This function restarts the game by clearing the window and showing the start screen.
  """
  global start
  start = False
  clear_window()
  show_start()

def play():
  """
  This function starts the game by setting the start variable to True 
  and showing the menu screen.
  """
  global start
  start = True
  show_menu() 

def change_settings():
  """
  This function displays the settings the user can change.
  """
  clear_window()
  
  # add settings frame
  settings_frame = new_frame(window)
  settings_frame.pack()
  
  # add color change buttons
  color_label = new_label(settings_frame, "Hangman Colors:")
  color_label.pack()
  
  body_color_button = new_button(settings_frame, "Body Color", change_body_color)
  body_color_button.pack()
  
  lines_color_button = new_button(settings_frame, "Lines Color", change_lines_color)
  lines_color_button.pack()
  
  text_color_button = new_button(settings_frame, "Text Color", change_text_color)
  text_color_button.pack()

  back_button = new_button(settings_frame, "Return to Home Screen", return_to_home)
  start = False
  back_button.pack()
  
  
def show_start():
  """
  This function shows the start screen with the welcome message, 
  hangman image, and play button.
  """
  global window, intro_frame

  if not window:
    # make the window
    window = Tk()
    window.title("Hangman")

  # add start frame
  intro_frame = new_frame(window)
  intro_frame.pack()
  
  # intro msg
  welcome_label = new_label(intro_frame,"Welcome to Hangman!")
  welcome_label.pack()

  # show hangman on view
  full_hangman(intro_frame)

  # put play button on view
  play_button = new_button(intro_frame,"Play", play)
  play_button.pack()

    # add a settings button for changing settings
  settings_button = new_button(intro_frame, "Settings", change_settings)
  settings_button.pack()
  

def end():
  """
  This function ends the game by clearing the window and destroying it.
  """
  clear_window()
  window.destroy()
  
def return_to_home():
  """
  This function returns to the home screen by clearing the window
  and showing the start screen.
  """
  clear_window()
  show_start()
  
def full_hangman(root):
  """
  This function displays the full hangman image on the screen.
  :param root: The parent window/frame for the hangman image.
  """
  for i in range(len(HANGMAN_INTRO)):
    hangman_line = new_label(root,HANGMAN_INTRO[i])
    hangman_line.pack()

def get_curr_hangman():
  """
  This function updates the hangman image based on the number of incorrect guesses.
  """
  global hangman_labels, last_int
  start_int = last_int
  stop_int = 6
  
  # add needed parts to starting hangman
  for i in range(start_int, stop_int):
    if i <= len(incorrect):
      line = HANGMAN_START[i] + HANGMAN_ADD[i]
      hangman_labels[i].config(text=line)
      last_int = i # change last int for next concatenation
  
def show_menu():
  """
  This function shows the menu screen with category choices for the user to select.
  """
  global start
  clear_window()

  # menu
  choose_label = new_label(window,"Choose a Word Set:")
  choose_label.pack()

  # put category choices on screen and start game based on user option
  for category in CATEGORIES:
    category_button = new_button(window, category, lambda category=category: start_game(category))
    category_button.pack()
   
  back_button = new_button(window, "Return to Home Screen", return_to_home)
  start = False
  back_button.pack()

def check_lose():
  """
  This function displays a message box to inform the user
  that they lost and shows the correct word.
  Asks the user if they want to play again.
  """
  alert_msg("Game Over!", "You lost. The word was: " + secret)
  ask_user_for_replay()
  
def process_input():
  """
  This function processes the user's guess, checks if it is valid,
  and updates the game state accordingly.
  """
  global lives_label, word_label, lives_rem, incorrect, part_of_word_guessed

  # checks if user did not enter a letter and informs 
  # the user of an invalid input
  if len(guess) > 1 or len(guess) == 0:
    alert_msg("Invalid Guess", "Only type one letter!")
    new_text = "Lives remaining: " + str(lives_rem)
    lives_label.config(text=new_text)
    return

  # checks if user repeated a prior inputted letter and informs 
  # the user of an invalid input
  if guess in incorrect or guess in part_of_word_guessed:
    get_curr_hangman()
    alert_msg("Invalid Guess", "Letter already attempted! Choose another one")
    new_text = "Lives remaining: " + str(lives_rem)
    lives_label.config(text=new_text)
    return

  # checks if user got a letter in the word
  if guess in secret.lower():
    for i in range(len(secret)):
        # looks for where guess character equals secret character(s)
        # and adds them to parts of the secret word guessed
        if secret[i].lower() == guess:
            part_of_word_guessed[i] = guess
          
    # updates word label to current parts of the secret
    # guessed
    new_word ="Word: " + " ".join(part_of_word_guessed)
    word_label.config(text=new_word)
    get_curr_hangman()
    alert_msg("Correct Guess", "Keep it up!")

    # checks if user has won or lost game  
    if "__ " not in part_of_word_guessed:
      check_win()
    return

  else: # adds incorrect letter to incorrect guesses set
    incorrect.add(guess)
    lives_rem -= 1
    new_text = "Lives remaining: " + str(lives_rem)
    lives_label.config(text=new_text)
    get_curr_hangman()
    alert_msg("Invalid Guess", "Letter is not in word")

    if lives_rem == 0:
      check_lose()

    return

def start_game(category):
  """
  This function starts a new game with the selected word category.
  :param category: The selected word category.
  """
  global lives_rem, incorrect, part_of_word_guessed, guess, lives_label, word_label, secret, guess_entry, game_frame, last_int
  clear_window()

  # add game frame
  game_frame = new_frame(window)
  game_frame.pack()
  
  # category display
  category_label = new_label(game_frame, "Selected Category: " + category)
  category_label.pack()

  # get list of words for specific category
  word_list = WORDS[category]

  # pick secret word from category options
  secret = get_random_word(word_list)

  # set new game variables
  lives_rem = MAX_NUM_GUESSES
  incorrect = set()
  part_of_word_guessed = ["__ "] * len(secret)
  last_int = 1

  # get rid of spaces
  for i in range(len(secret)):
    if secret[i] == " ":
      part_of_word_guessed[i] = " "

  # set on screen views/display
  lives_label = new_label(game_frame,"Lives remaining: " + str(lives_rem))
  lives_label.pack()
  word_label = new_label(game_frame,"Word: " + " ".join(part_of_word_guessed))
  word_label.pack()
  
  # put start hangman on display
  config_hangman(game_frame) 
  # add color settings to hangman
  update_hangman_colors()
  
  # guess prompt
  guess_label = new_label(game_frame,"Enter your guess:")
  guess_label.pack()

  # text entry
  guess_entry = new_entry(game_frame,("Arial", 14))
  guess_entry.pack()

  # submit guess button
  submit_button = new_button(game_frame,"Submit", submit_guess)
  submit_button.pack()
  guess_entry.bind("<Return>", lambda event: submit_guess())

def submit_guess():
  """
  This function retrieves the user's guess from the input field and processes it.
  """
  global guess
  # retrieve user input
  guess = guess_entry.get().strip().lower()
  guess_entry.delete(0, END)
  process_input()

def check_win():
  """
  This function displays a message box to inform the user that 
  they won and asks user if they want to play again.
  """
  if lives_rem > 0:
    alert_msg("Congratulations!", "You won!")
    ask_user_for_replay()
    
def ask_user_for_replay():
  """
  This function asks the user if they want to play again.
  """
  clear_window()
  
  # add play again frame
  play_again_frame = new_frame(window)
  play_again_frame.pack()
  
  # label question display
  prompt_label = new_label(play_again_frame, "Would you like to play again?")
  prompt_label.pack()
  
  # yes and no buttons
  yes_button = new_button(play_again_frame,"Yes", play_again)
  yes_button.pack()
  no_button = new_button(play_again_frame,"No", end)
  no_button.pack()
    
def get_random_word(word_list):
  """
  This function returns a random word from the given list of words.
  :param word_list: The list of words.
  :return: A random word from the list.
  """
  return random.choice(word_list)

def run():
  """
  Runs the entire game window
  """
  show_start()
  if start:
    show_menu()
  window.mainloop()
  
if __name__ == "__main__":
  run()
