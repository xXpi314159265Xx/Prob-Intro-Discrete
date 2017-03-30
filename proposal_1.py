# In this game the letters l,i,o,n,s are written on a ball.
# The player draws two balls and if the letters spell a word
# in any order, the player is a winner.

import random

def draw_balls(letters):
	'''INPUT: list of available letters written on balls
		OUTPUT: letters chosen from two balls drawn'''
	ball_1 = random.choice(letters)
	letters.remove(ball_1)
	ball_2 = random.choice(letters)
	letters.append(ball_1)
	return ball_1, ball_2

	
def check_letters(letter_list, word_list):
	'''INPUT: List of letters and list of words
	OUTPUT: True if the two letters form a word and the word itself.'''
	ball_1, ball_2 = draw_balls(letter_list)
	word_1 = ball_1 + ball_2
	word_2 = ball_2 + ball_1
	if word_1 in word_list:
		return True, word_1, ball_1, ball_2
	elif word_2 in word_list:
		# return True if order doesn't matter
		return False, word_2, ball_1, ball_2
	else:
		return False, word_1, ball_1, ball_2
		

def many_games(number, letter_list, word_list):
	'''INPUT: Number of games to play, letters to draw and word list
	OUTPUT: Number of games won and played'''
	total_games = 0
	games_won = 0
	while number > 0:
		a, b, ball_1, ball_2 = check_letters(letter_list, word_list)
		total_games += 1
		if a == True:
			games_won += 1
			#print(ball_1, ball_2)
		number -= 1
	return games_won, total_games
	
def one_game(letter_list, word_list):
	'''INPUT: List of letters to draw and list of legal words
	OUTPUT: The letters drawn and whether or not they form a legal word.'''
	a, b, ball_1, ball_2 = check_letters(letter_list, word_list)
	print("You drew a ball with the letters:")
	print("%s and %s" %(ball_1, ball_2))
	if a == True:
		print("The letters %s and %s form the word %s" %(ball_1, ball_2, b))
	else:
		print("Sorry! The letters %s and %s do not form a legal word." %(ball_1, ball_2))
		print("You lose!")
	print()

	
def main():
	number_of_games = int(input("How many games do you want to play?\n"))
	print()
	while True:
		# Can change game by editing two lists below
		letters = ['l','i','o','n','s']
		words = ['in', 'no', 'on', 'so', 'is']
		lo_a_word = False
		if lo_a_word:
			words.append('lo')
		if number_of_games == 1:
			one_game(letters, words)
			choice = input("Would you like to play again? 'y' or 'n'")
			if choice == 'n':
				print()
				print("Thanks for playing!")
				break
		else:
			wins, total = many_games(number_of_games, letters, words)
			print("You played %s games and won %s of them." %(total, wins))
			break
		print()
		
	
main()
