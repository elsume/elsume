import random

import dice
import player


# ** is just a print statement that is used to keep track of player's info throughout the game
class Game(dice.Dice):
    player_list = []
    num_turns = 0

    def __init__(self, num_players, num_chips):
        self.num_chips = num_chips
        self.num_players = num_players

    # method that creates instances of the player class which has the player's name and their number of points as attributes
    def get_players(self):
        for num in range(1, self.num_players + 1):
            while True:
                try:
                    player_name = str(input(f"Enter player {num}'s name: "))
                    break
                except ValueError:
                    print("Input is not an integer.")
            self.player_list.append(player.Player(player_name, self.num_chips))

    # method that simulates a turn in the game
    def start_round(self):
        for player in self.player_list:
            # print(f"{player}'s turn with {player.points} points:")  # **
            if player.points > 0:
                self.num_turns += 1
                rolls = self.dice_roll(
                    player.points
                )  # checks how many points the player has and rolls the corresponding amount of times
                for roll in rolls:
                    player.turn(
                        roll
                    )  # goes through roll results and adds and subtracts points from players accordingly
            elif player.points == 0:
                player.turns_without_points += 1
                if player.turns_without_points < 2:
                    # print(f"{player} has no points so their dice roll is passed.")  # **
                    self.num_turns += 1
                elif player.turns_without_points == 2:
                    # print(
                    #     f"{player} has been passed twice so they are taken out of the game."
                    # )  # **
                    self.player_list.remove(player)
            # print()  # **
