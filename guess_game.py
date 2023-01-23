#import the neccessary modules
import random
from art import logo

#define a variable that stores the difficulty level
EASY_LEVEL = 10
HARD_LEVEL = 5

#create a function that compares the result
def compare_result(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"That is right the anwer was {answer}. you win.")


#create a function for the difficulty
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL


#create a function that plays the game
def play_game():
    print(logo)
    print("Welcome to Guess game.")
    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    # print(f"pssst. the answer is {answer}")

    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #prompt for user to guess a number the computer is thinking

        guess = int(input("Make a guess: "))

        #check if the answer matches the computer input by return the compare function

        turns = compare_result(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses. You lose")
            return
        elif guess != answer:
            print("Guess again.")
play_game()
