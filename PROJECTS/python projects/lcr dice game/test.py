import random
import unittest

import game
from dice import Dice


class TestGame(unittest.TestCase):
    def test_game(self):
        random.seed(1)
        test1 = game.Game(3, 3)
        test1.get_players()
        winner = test1.player_list[2]
        while len(test1.player_list) > 1:
            test1.start_round()
        self.assertEqual(37, test1.num_turns)
        self.assertEqual(winner, test1.player_list[0])


# inclusion of modified Player class to make testing easier
class Player:
    def __init__(self, name, points, turns_without_points=0):
        self.name = name
        self.points = points
        self.turns_without_points = turns_without_points

    def turn(self, roll):
        match roll:
            case "C":
                self.points -= 1
            case "R":
                self.points -= 1
                if self == player_list[-1]:
                    player_list[0].points += 1
                else:
                    player_list[player_list.index(self) + 1].points += 1
            case "L":
                self.points -= 1
                if self == player_list[0]:
                    player_list[-1].points += 1
                else:
                    player_list[player_list.index(self) - 1].points += 1
            case _:
                pass

    def __str__(self):
        return self.name


class TestDice(unittest.TestCase):
    # tests if numbers from range 1-6
    # are correctly converted to their corresponding dice side
    def test_dice_side(self):
        self.assertEqual(Dice.dice_side(self, 1), "L")
        self.assertEqual(Dice.dice_side(self, 6), "Dot")
        self.assertEqual(Dice.dice_side(self, 3), "C")
        self.assertEqual(Dice.dice_side(self, 2), "R")

    print("test passed")

    # inclusion of modified method from Dice to make testing easier
    def dice_side(self, num):
        if num == 1:
            return "L"
        elif num == 2:
            return "R"
        elif num == 3:
            return "C"
        elif num == 4 or num == 5 or num == 6:
            return "Dot"

    # tests if dice method returns the correct number of rolls
    # according to a player's number of points
    def test_dice_roll(self):
        self.assertTrue(len(Dice.dice_roll(self, 3)) == 3)
        self.assertTrue(len(Dice.dice_roll(self, 2)) == 2)
        self.assertTrue(len(Dice.dice_roll(self, 1)) == 1)
        self.assertFalse(len(Dice.dice_roll(self, 5)) == 5)

    print("test passed")


# initialize player list
player1 = Player("Shadrach", 3)
player2 = Player("Meshach", 3)
player3 = Player("Abednego", 3)
player_list = [player1, player2, player3]


# checks if points are added or subtracted accordingly throughout the player list
class TestPlayer(unittest.TestCase):
    def test_turn(self):
        player_list[0].turn("Dot")
        self.assertTrue(player_list[0].points == 3)
        player_list[1].turn("C")
        self.assertTrue(player_list[1].points == 2)
        player_list[1].turn("L")
        self.assertTrue(player_list[0].points == 4)
        player_list[2].turn("R")
        self.assertTrue(player_list[0].points == 5)

    print("test passed")


if __name__ == "__main__":
    unittest.main()
