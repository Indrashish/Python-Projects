# Python script to simulate functionality of a rolling dice

# Ask user if willing to roll the die. If yes, then dice will roll and come up with a number between 1 and 6.
# Continue as long as user ready to play

import random

class DiceRollingSimulator:
    def rolldice(self, minimum, maximum):
        output = random.randint(minimum, maximum)
        print("Output: ", output)

    def main(self):
        while True:
            # We ask user if they want to use the calculator further
            user_input = int(input("Do you want to roll the dice? 1. Yes 2. No \n"))

            if (user_input != 1):
                print("Exit Dice Rolling.....")
                break
            else:
                self.rolldice(1, 6);

dice_sim = DiceRollingSimulator()
dice_sim.main()