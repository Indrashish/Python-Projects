
# The Goal: The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words,
# the user needs to be able to input information.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too
# low). If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number, to see the difference between
# the inputted number and the randomly generated numbers, and to then compare the numbers.

import random

class GuessNumber:
    def generate(self):
        return random.randint(-10000, 10000)

    def determine_guess(self, prog_guess, user_num_guess):
        #print("Number guessed by program", prog_guess)
        diff = user_num_guess - prog_guess
        if diff == 0:
            print("Bingo!!!! your guess is right")
            exit()
        elif 0 < diff < 100:
            print("Your guess is high")
        elif diff >= 100:
            print("Your guess too high")
        elif -100 < diff < 0:
            print("Your guess is low")
        elif diff <= -100:
            print("Your guess is too low")
        else:
            raise Exception("Input character not supported")

    def main(self):
        prog_guess = self.generate()
        while True:
            # We ask user if they want to guess further
            user_input = int(input("Do you want to guess? 1. Yes 2. No \n"))

            if (user_input != 1):
                print("Exiting .....")
                break
            else:
                user_num_guess = int(input("Please enter the number \n"))
                self.determine_guess(prog_guess, user_num_guess)

guess_num = GuessNumber()
guess_num.main()