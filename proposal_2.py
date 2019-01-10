# In this game the contestant chooses two different numbers
# between 1 and 9, inclusive. Then two different numbers betweeen
# 1 and 9 are generated at random. The contestant wins if both
# numbers match exactly.

import random, os

def player_numbers():
    player_number_list = []
    number_1 = int(input("Choose a number from 1 to 9.\n"))
    number_2 = int(input("Choose a different number from 1 to 9.\n"))
    assert number_1 != number_2
    player_number_list.append(number_1)
    player_number_list.append(number_2)
    return sorted(player_number_list)


def game_numbers():
    number_1, number_2 = 5,5
    game_number_list = []
    while number_1 == number_2:
        number_1 = random.randint(1,9)
        number_2 = random.randint(1,9)
    game_number_list.append(number_1)
    game_number_list.append(number_2)
    return sorted(game_number_list)


def one_game():
    response = 'y'
    while response == 'y':
        os.system('cls')
        player = player_numbers()
        game = game_numbers()
        print()
        print("The numbers drawn are:")
        print("%i and %i" %(game[0], game[1]))
        print()
        if player == game:
            print("You won!")
        else:
            print("Sorry. You lose.")
        response = input("Type 'y' to play again or press any key to exit.\n")


def many_games(number):
    wins = 0
    print()
    print("Choose the numbers that you want to play all of your games with.")
    print()
    player = player_numbers()
    while number > 0:
        game = game_numbers()
        if player == game:
            wins += 1
        number -= 1
    return wins


def main():
    print()
    number_of_games = int(input("How many games would you like to play?\n"))
    assert number_of_games > 0
    if number_of_games == 1:
        one_game()
    else:
        wins = many_games(number_of_games)
        print()
        print("You played %i games and won %i of them." %(number_of_games, wins))

main()