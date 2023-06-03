# The Hangman Game (with Python/Tkinter)

This project is a Hangman game implemented using the Tkinter library in Python. The objective of the game is to guess a secret word within a limited number of attempts. The game follows the traditional rules of Hangman:

The player has a limited number of guesses to correctly guess the letters in the secret word.
For each incorrect guess, a part of the hangman's body is added.
If the hangman's body is complete before the word is guessed, the player loses.
If the player correctly guesses all the letters in the word before the hangman is complete, the player wins.
The game provides various word categories to choose from, such as fruits, flowers, places, animals, colors, countries, sports, movies, and professions. The player can select a category, and a secret word from that category will be chosen randomly for the game.

The game interface is created using the Tkinter library, with buttons and keyboard inputs for interacting with the game. The user can input a single letter as a guess using the keyboard and the ENTER key. Mouse inputs are used to click buttons for starting the game, selecting word categories, and playing again.

The game screen displays the hangman image, the secret word represented by underscores, the number of lives remaining, and the incorrect letters guessed so far. The player can continue making guesses until they either win or lose the game. If the player wins, a message will be displayed, and they will have the option to play again. If the player loses, the correct word will be revealed, and they will also have the option to play again.

Additionally, the game includes a settings menu where the player can change the colors of the hangman's body, lines, and text. This feature allows for customization of the game's visual appearance.

Overall, this Hangman game provides an enjoyable and interactive experience for players to test their word-guessing skills.
