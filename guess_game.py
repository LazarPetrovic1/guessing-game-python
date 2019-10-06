
from random import randint

def gg():
	x = randint(0, 101)
	y = input("Enter a number between 0 and 101: ")
	guesses = 10
	while int(y) != x and guesses > 0:
		if int(y) < x:
			y = input("Your estimate is too low. Go higher. ")
		elif int(y) > x:
			y = input("Your estimate is too high. Go lower. ")
		guesses -= 1
		if int(y) == x:
			print("That is correct!")
			z = input("Do you want to play again? y/n ")
			if z == "y":
				gg()
			else:
				break
			break
		elif guesses <= 0:
			print("You've lost. The correct answer was {}".format(x))
			z = input("Do you want to play again? y/n ")
			if z == "y":
				gg()
			else:
				break

gg()
