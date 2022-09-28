#w4rm15h
#50 Projects
#6. Rock, Paper, Scissors

import os
import time
import random
from termcolor import colored

titles = {
	'vs' : """
					██╗░░░██╗░██████╗
					██║░░░██║██╔════╝
					╚██╗░██╔╝╚█████╗░
					░╚████╔╝░░╚═══██╗
					░░╚██╔╝░░██████╔╝
					░░░╚═╝░░░╚═════╝░""",
	
	'win' : """
			  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
			  ░██║░░██╗░░██║██║████╗░██║██║
			  ░╚██╗████╗██╔╝██║██╔██╗██║██║
			  ░░████╔═████║░██║██║╚████║╚═╝
			  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
			  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝""",
	
	'loose' : """
		  ██╗░░░░░░█████╗░░█████╗░░██████╗███████╗
		  ██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔════╝
		  ██║░░░░░██║░░██║██║░░██║╚█████╗░█████╗░░
		  ██║░░░░░██║░░██║██║░░██║░╚═══██╗██╔══╝░░
		  ███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗
		  ╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝""",
	
	'draw' : """
		  ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
		  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
		  ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
		  ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
		  ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
		  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░""",

	'rock' : """	
			 ██████╗░░█████╗░░█████╗░██╗░░██╗
			 ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
			 ██████╔╝██║░░██║██║░░╚═╝█████═╝░
			 ██╔══██╗██║░░██║██║░░██╗██╔═██╗░
			 ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
			 ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝""",
	'paper' : """
		 ██████╗░░█████╗░██████╗░███████╗██████╗░
		 ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
		 ██████╔╝███████║██████╔╝█████╗░░██████╔╝
		 ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
		 ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║
		 ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝""",
	'scissors' : """
░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░""",}#59


#VARIABLES
class vars():
	playerName = "Player 1"
	aiName = "CHEESE"
	playerScore = 0
	aiScore = 0
	
#MOVE LIST
moves = {
	"1": "rock",
	"2": "paper",
	"3": "scissors",
}

def result(result, colour, phrase):
	os.system("clear")
	r = titles[result]
	print(colored(r, f'{colour}'))
	print(colored(f"{phrase}".center(59), 'cyan'))
	if result == "win":
		
		vars.playerScore += 1
	else:
		if result == "loose":
			vars.aiScore += 1
			
	time.sleep(2)

#FUNCTIONS
def printingTitle():
	os.system("clear")
	rock = colored(titles['rock'], 'green')
	paper = colored(titles['paper'], 'red')
	scissors = colored(titles['scissors'], 'blue')
	print(f"{rock}{paper}{scissors}")
	print(colored(f"[{vars.playerName}: {vars.playerScore}][{vars.aiName}: {vars.aiScore}]".center(58), 'green'))

#BATTLE ROYAL
def battleRoyal(player, ai):
	print(colored(titles[player], 'green'))
	time.sleep(0.5)
	print(colored(titles["vs"], 'red'))
	time.sleep(0.5)
	print(colored(titles[ai], 'blue'))
	time.sleep(2)

#MAIN FUNCTION
def rockPaperScissors():
	while True:
		printingTitle()
		print()
		print("1. Rock")
		print("2. Paper")
		print("3. Scissors")		
		move = input("[1, 2 or 3]: ")
		if move not in("1","2","3"):
			print("maybe just choose a valid option")
		#GETTING STARTED
		else:
			player = moves[move]
			ai = random.choice(list(moves.values()))			
			battleRoyal(player, ai)
			
			#ALRIGHT ALRIGHT ALRIGHT
			if player == ai:
				result('draw', 'blue', '***DRAW***')
			#IF ROCK
			elif player == "rock":
				if ai == "scissors":
					result('win', 'green', "Rock smashes scissors!")
				else:
					result('loose', 'red', "Paper covers rock!")
			#IF PAPER
			elif player == "paper":
				if ai == "rock":
					result('win', 'green', "Paper covers rock! You win!")
				else:
					result('loose', 'red', "Scissors cuts paper!")
			#IF SCISSORS	
			elif player == "scissors":
				if ai == "paper":
					result('win', 'green', "Scissors cuts paper! You win!")
				else:
					result('loose', 'red', "Rock smashes scissors! You lose.")
				
#GREETING MENU
def welcomeScreen():
	printingTitle()
	print("\nWelcome to Rock Paper Scissors")
	print("Shall we get cracking?")
	while True:
		play = input("[y/n?]: ")
		if play not in("y", "n"):
			print("C'mon, it's not that hard")
		else:
			if play == "y":
				break
			else:
				print("Alright, quitting the game")
				exit()
				
	while True:
		name = input("Enter your name: ")
		sure = input(f"Are you happy with {name}?\n[y/n]? ")
		if sure not in ("y", "n"):
			print("y or n?")
		else:
			if sure == 'y':
				vars.playerName = name
				print(f"Alright {name}, one more thing...")
				break
			else:
				print(f"Alright, try again {name}")
				time.sleep(1)

	while True:
		name = input("Name your opponent: ")
		sure = input(f"Are you happy with {name}?\n[y/n]? ")
		if sure not in ("y", "n"):
			print("y or n?")
		else:
			if sure == 'y':
				vars.aiName = name
				print(f"Alright {vars.playerName}, let's get going...")
				time.sleep(1)
				rockPaperScissors()
			else:
				print(f"Alright, try again {name}")
				time.sleep(1)		


if __name__ == "__main__":
	welcomeScreen()




