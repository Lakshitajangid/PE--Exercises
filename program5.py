import random

def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total_score = dice_1 + dice_2

    print(f"You rolled a {dice_1} and a {dice_2}. Your total score is {total_score}.")

def play_game():
    print("Welcome to the Dice Game!")
    print("Click the \"Roll Dice\" button to roll the dice and find out your score.")
    input("Press Enter to roll the dice.")

    roll_dice()

play_game()
