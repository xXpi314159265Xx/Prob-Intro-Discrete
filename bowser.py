# The letters in BOWSER are written on balls
# The player can
# 1. Pay to have two balls chosen and if a legal word
#   is spelled in the order the balls were drawn, they
#   win a prize.
# 2. Pay to have three balls chosen and win if a legal
#   word is spelled in the order the letters were drawn.
#
# In this version, players can win twice if the letters
# drawn spell both a two and three letter word.

import random

letters = ["b", "o", "w", "s", "e", "r"]
two_letter_words = ["be", "so", "we", "or"]
three_letter_words = ["bow","bro","orb","rob","row","sob","sow","sew","web","ore","owe"]

def draw_two(letters):
    word = ''
    random_choice = random.sample(letters, draw)
    for i in range(draw):
        word += random_choice[i]
    #print(word)
    if word in two_letter_words:
        print("You win.")
        return 1
    else:
        print("You lost.")
        return 0

def draw_three():
    word = ''
    letters = ["b", "o", "w", "s", "e", "r"]
    letter_1 = random.choice(letters)
    letters.remove(letter_1)
    letter_2 = random.choice(letters)
    letters.remove(letter_2)
    word_2 = letter_1 + letter_2
    letter_3 = random.choice(letters)
    word_3 = word_2 + letter_3
    #print(word_2, word_3)
    if word_2 in two_letter_words:
        if word_3 in three_letter_words:
            #print("You won twice.")
            win_2, win_3 = 1, 1
        else:
            #print("You got a two letter, not a three letter word.")
            win_2, win_3 = 1, 0
    elif word_3 in three_letter_words:
        #print("You got a three letter word, not a two letter word.")
        win_2, win_3 = 0, 1
    else:
        #print("You didn't get a two or three letter word.")
        win_2, win_3 = 0, 0
    return win_2, win_3


number_of_games = int(input("How many games would you like to play?\n"))
draw = int(input("How many letters would you like to draw for each of these games, 2 or 3?\n"))

def play_games(number_of_games, draw):
    total = number_of_games
    two_letter_wins = 0
    three_letter_wins = 0
    double_wins = 0
    while number_of_games > 0:
        if draw == 2:
            two_letter_wins += draw_two(letters)
        else:
            win_2, win_3 = draw_three()
            if win_2 == 1 and win_3 == 1:
                double_wins += 1
            else:
                two_letter_wins += win_2
                three_letter_wins += win_3
        number_of_games -= 1
    if draw == 3:
        print()
        print("RESULTS")
        print()
        print("TWO WINNING WORDS")
        print("You had both a two letter and three letter word {} times.".format(double_wins))
        print()
        print("ONLY ONE WINNING WORD")
        print("You had a winning three letter word {} times.".format(three_letter_wins))
    print("You a winning two letter word {} times.".format(two_letter_wins))
    print()
    print("STATS")
    print()
    print("You won with both a two and three letter word {} percent of the time.".format(round((double_wins/total)*100,2)))
    print("You won with only a two letter word {} percent of the time.".format(round((two_letter_wins/total)*100,2)))
    print("You won with only a three letter word {} percent of the time.".format(round((three_letter_wins/total)*100,2)))

play_games(number_of_games, draw)
