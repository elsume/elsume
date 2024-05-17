import random

import game

# collects value used for random seed and checks if user input is valid
while True:
    try:
        random.seed(int(input("Please enter a seed: ")))
        break
    except ValueError:
        print("Error! That is not a valid input!")

# checks if user input is valid
while True:
    try:
        num_players = int(input("How many players are going to play?: "))
        while num_players <= 2:
            num_players = int(
                input("Game needs more players, please enter another number: ")
            )
        break
    except ValueError:
        print("Input is not an integer.")

while True:
    try:
        num_chips = int(input("How many chips will they start with?: "))
        while num_chips <= 2:
            num_chips = int(
                input("Game needs more chips, please enter another number: ")
            )
        break
    except ValueError:
        print("Input is not an integer.")

play = game.Game(num_players, num_chips)
play.get_players()

while len(play.player_list) > 1:
    play.start_round()
print(
    f"{play.player_list[0]} is the last player standing after {play.num_turns} turns."
)
