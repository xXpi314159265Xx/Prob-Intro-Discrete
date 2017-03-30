# In this game the contestant bets $1 on a number between 1 and 6.
# The contestant then rolls two dice and wins an additional $1 for
# each time the dice shows the chosen number. However, if neither of
# the dice has the number, the contestant loses the dollar.

import random

def roll_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    return dice_1, dice_2


def check_dice(player_number,dice_1,dice_2):
    if dice_1 == player_number and dice_2 == player_number:
        winnings = 2
    elif dice_1 == player_number or dice_2 == player_number:
        winnings = 1
    else:
        winnings = -1
    return winnings


def one_game():
    response = 'y'
    while response == 'y':
        number = int(input("What number do you choose?\n"))
        assert 0 < number < 7
        print()
        dice_1, dice_2 = roll_dice()
        print("You rolled a %i and a %i." %(dice_1,dice_2))
        print()
        winnings = check_dice(number,dice_1,dice_2)
        if winnings > 0:
            print("You won $%i!" %(winnings))
        else:
            print("Sorry. You lost your $1.")
        print()
        response = input("Type 'y' to play again or press any key to quit.\n")

def many_games(number):
    winnings = 0
    games_won_1 = 0
    games_won_2 = 0
    game_number = int(input("What number would you like to use for all games?\n"))
    assert 0 < game_number < 7
    while number > 0:
        dice_1, dice_2 = roll_dice()
        #print(dice_1,dice_2)
        result = check_dice(game_number,dice_1,dice_2)
        if result == 1:
            games_won_1 += 1
        elif result == 2:
            games_won_2 += 1
        winnings += result
        number -= 1
    return winnings, games_won_1, games_won_2


def main():
    print()
    games = int(input("How many games would you like to play?\n"))
    print()
    if games == 1:
        one_game()
    else:
        money, games_won_1, games_won_2 = many_games(games)
        print("You played %i games." %(games))
        print()
        print("You won $1 in %i games." %(games_won_1))
        print("You won $2 in %i games for a total of $%i." %(games_won_2,games_won_2*2))
        print("You lost $1 in %i games." %(games-games_won_1-games_won_2))
        print()
        if money < 0:
            print("Overall, you lost a total of $%i." %(money*-1))
        else:
            print("Overall, you won a total of $%i." %(money))


main()