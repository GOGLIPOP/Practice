import os
import random


def game(difficulty, attempts):
    os.system("cls")
    print(f'You have {attempts} attempts remaining to guess the number.')
    secret_number = random.randint(1, 100)
    while attempts > 0:

        guess = ''
        while not isinstance(guess, int):
            try:
                guess = int(input("Make a guess: "))
            except UnboundLocalError and ValueError:
                ...

        proba = secret_number - guess
        if proba <= 5 and proba >= -5:
            os.system("cls")
            print("Near(+-5)")
        elif proba > 5:
            os.system("cls")
            print('To low')
        elif proba < 0:
            os.system("cls")
            print('To high')

        attempts -= 1
        if guess == secret_number:
            os.system("cls")
            print(f"Yes, it's {secret_number}, congratulations, you win!")
            return
        print(f"You have {attempts} attempts remaining to guess the number!")
    print(f"You lose, try again!(Guessed number is {secret_number})")


def difficulty_func():
    global attempts
    attempts = 0
    difficulty = str(input("Choose a difficulty. Type 'Easy', 'Normal' or 'Hard': ").lower())
    while difficulty != 'easy' and difficulty != 'normal' and difficulty != 'hard':
        difficulty = str(input("Choose a difficulty. Type 'Easy' or 'Normal' or 'Hard': ").lower())
    else:
        if difficulty == 'easy':
            attempts += 10
        elif difficulty == 'normal':
            attempts += 5
        elif difficulty == 'hard':
            attempts += 3
    game(difficulty, attempts)


print('welcome to the number guessing game!(The number can be 1-100)'.title())
difficulty_func()
input("Press enter to exit...")


