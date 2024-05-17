import random


class Dice:
    def dice_side(self, num):
        if num == 1:
            return "L"
        elif num == 2:
            return "R"
        elif num == 3:
            return "C"
        elif num == 4 or num == 5 or num == 6:
            return "Dot"

    def dice_roll(self, num_chips):
        roll = []
        if num_chips >= 3:
            for i in range(0, 3):
                side = self.dice_side(random.randint(1, 6))
                roll.append(side)
        elif num_chips < 3:
            for i in range(0, num_chips):
                side = self.dice_side(random.randint(1, 6))
                roll.append(side)
        # for i in roll:
        #     print(f"{i} has been rolled.")  # **
        return roll
