import game


class Player:
    def __init__(self, name, points, turns_without_points=0):
        self.name = name
        self.points = points
        self.turns_without_points = turns_without_points

    # switch method that adds and subtracts points according to the roll the player has
    def turn(self, roll):
        match roll:
            case "C":
                self.points -= 1
            case "R":
                self.points -= 1
                if self == game.Game.player_list[-1]:
                    game.Game.player_list[0].points += 1
                else:
                    game.Game.player_list[
                        game.Game.player_list.index(self) + 1
                    ].points += 1
            case "L":
                self.points -= 1
                if self == game.Game.player_list[0]:
                    game.Game.player_list[-1].points += 1
                else:
                    game.Game.player_list[
                        game.Game.player_list.index(self) - 1
                    ].points += 1
            case _:
                pass

    # lets program print player name as a string
    def __str__(self):
        return self.name
