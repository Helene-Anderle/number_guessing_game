
from random import randint

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""



turns_hard = 5
turns_easy = 10


def choice():
    user_choice = input("Do you want the easy or hard version? Type easy or hard: ")
    if user_choice == "easy":
        return turns_easy
    else:
        return turns_hard

def check(u_answer, a_answer, turns):
    if u_answer > a_answer:
        print("\033[1mGuess lower⬇️\033[0m")
        return turns -1
    elif u_answer < a_answer:
        print("\033[1mGuess higher⬆️\033[0m")
        return turns -1
    else:
        print("You got it right! Congratulations!🎉")

def play():
    print (logo)
    print("Welcome to the guess a number game!👋 ")
    print("I am thinking of a number between 0 and 100, can you guess which one?")
    solution = randint(1, 100)

    turns = choice()
    guess = 0
    while guess != solution:
        print(f"You have {turns} guesses left to guess the correct answer")
        guess = int(input("Guess a number: "))
        turns = check(guess, solution, turns)
        if turns == 0:
            print("You have run out of guesses.")
            print(f"The right answer would have been {solution}")
            return
        elif guess != solution:

            print ("Try another guess")



play()
