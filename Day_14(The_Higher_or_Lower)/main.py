from art import logo, vs
from game_data import data
import random
import os


def start(player_score, first):
    os.system('Cls')
    print(logo)

    second = random.choice(data)

    if player_score >= 1:
        print(f"You're right! Current score: {player_score}")
    else:
        first = random.choice(data)

    while first == second:
        second = random.choice(data)

    if first["description"][0].lower() in "aoe":
        print(f"Compare A: {first['name']}, an {first['description']}, from {first['country']}.")
    else:
        print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}.")

    print(vs)

    if second["description"][0].lower() in "aoe":
        print(f"Against B: {second['name']}, an {second['description']}, from {second['country']}.")
    else:
        print(f"Against B: {second['name']}, a {second['description']}, from {second['country']}.")

    if first["follower_count"] > second["follower_count"]:
        winner = "a"

    else:
        winner = "b"
        first = second

    player_choice = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

    while player_choice not in "ab":
        player_choice = str(input("Error, Type 'A' or 'B': ")).lower()
    else:
        if winner == player_choice:
            player_score += 1
            start(player_score, first)
        else:
            print(f"Sorry, that's wrong. Final score: {player_score}")



start(player_score=0, first = '')
input("Press enter to exit...")

