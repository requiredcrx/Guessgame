# Guess Game
This is a Python program that simulates a guessing game. The program imports the random and art modules and uses them to generate a random number between 1 and 100 and display a logo art. The program prompts the user to choose a difficulty level, either 'easy' or 'hard', then generates a random number and prompts the user to guess the number. The program compares the user's guess to the generated number and provides feedback until the user correctly guesses the number or runs out of turns.

## Usage
To run the program, simply execute the guess_game.py script in a Python environment. The program will display the logo, prompt the user to choose a difficulty level, then generates a random number and prompts the user to guess the number. The program compares the user's guess to the generated number and provides feedback until the user correctly guesses the number or runs out of turns.

## Examples
### Easy level
```py
$ python guess_game.py
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
|     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

Welcome to Guess game.
I am thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard' easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low
You have 8 attempts remaining to guess the number.
Make a guess: 37
That is right the anwer was 37. you win.
```
### Hard level
```py
$ python guess_game.py
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____
|     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

Welcome to Guess game.
I am thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard' hard
You have 5 attempts remaining to guess the number.
Make a guess: 50
Too high
You have 4 attempts remaining to guess the number.
Make a guess: 25
Too low
You have 3 attempts remaining to guess the number.
Make a guess: 30
Too low
You have 2 attempts remaining to guess the number.
Make a guess: 35
Too low
You have 1 attempts remaining to guess the number.
Make a guess: 37
Too low
You have run out of guesses. You lose
```

## Note
In the provided script, there is a `return` statement in the `play_game()` function after the game ends with the user running out of turns. This means that the function will stop executing and return control to the caller, in this case the script's main execution context. The game will not start again after a loss. However, if you want the game to start again after a loss, you can use a loop or a recursion to call the `play_game()` function again.
This is part of my day 13 project of 100 days of Code.


