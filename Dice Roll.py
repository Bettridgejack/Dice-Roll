import random

dice = [1, 2, 3, 4, 5, 6]

def roll_dice(dice):
    return random.choice(dice)

def user_roll():
    roll = input("Would you like to roll the dice? y/n: ").lower()
    if roll == "y":
        print(roll_dice(dice))
    else:
        print("Gooodbye")

def main():
    while True:
        user_roll()
        play_again = input("Play again? y/n: ")
        if play_again == "n":
            break

main()
    

