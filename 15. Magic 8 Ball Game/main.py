#w4rm15h
#50 Projects
#15. Magic 8 Ball Game
import random
import os
import time

#Responses
responses = [
	"Don't count on it.",
	"My reply is no.",
	"My sources say no.",
	"Outlook not so good.",
	"Very doubtful.",
	"Reply hazy, try again.",
	"Ask again later.",
	"Better not tell you now.",
	"Cannot predict now.",
	"Think and ask again.",
	"As I see it, yes.",
	"Most likely.",
	"Outlook good.",
	"Yes.",
	"Signs point to yes.",
	"It is certain.",
	"It is decidedly so.",
	"Without a doubt.",
	"Yes definitely.",
	"You may rely on it.",
]

m8ballWelcome = """ 
///////////@@@@@@@@@////////////
//////@@@@@@@@@@@@@@@@@@@///////
////@@@@@@@@@@@@@@@@@@@@@@@@////
//@@@@@@@@@          @@@@@@@@@//
/@@@@@@@@    Ask       @@@@@@@@/
/@@@@@@@      me        @@@@@@@/
@@@@@@         a          @@@@@@
/@@@@@@@    question    @@@@@@@/
/@@@@@@@@        ????  @@@@@@@@/
//@@@@@@@@@          @@@@@@@@@//
////@@@@@@@@@@@@@@@@@@@@@@@/////
//////@@@@@@@@@@@@@@@@@@@///////
///////////@@@@@@@@@////////////"""

m8balltop = """ 
///////////@@@@@@@@@////////////
//////@@@@@@@@@@@@@@@@@@@///////
////@@@@@@@@@@@@@@@@@@@@@@@@////
//@@@@@@@@@          @@@@@@@@@//"""

m8ballbottom = """	
//@@@@@@@@@          @@@@@@@@@//
////@@@@@@@@@@@@@@@@@@@@@@@/////
//////@@@@@@@@@@@@@@@@@@@///////
///////////@@@@@@@@@////////////"""

space = "              "

ballAnswer = {
	"ball1": "              ",
	"ball2": "              ",
	"ball3": "              ",
	"ball4": "              ",
	"ball5": "              ",
	"startball1": "/@@@@@@@@",
	"startball2": "/@@@@@@@ ",
	"startball3": "@@@@@@   ",
	"startball4": "/@@@@@@@ ",
	"startball5": "/@@@@@@@@",
	"endball1": " @@@@@@@/",
	"endball2": "  @@@@@@/",
	"endball3": "   @@@@@@",
	"endball4": "  @@@@@@/",
	"endball5": " @@@@@@@/",
	"finball1": "",
	"finball2": "",
	"finball3": "",
	"finball4": "",
	"finball5": "",
}

#42 CHARS
title = """
░█████╗░  ██████╗░░█████╗░██╗░░░░░██╗░░░░░
██╔══██╗  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░
╚█████╔╝  ██████╦╝███████║██║░░░░░██║░░░░░
██╔══██╗  ██╔══██╗██╔══██║██║░░░░░██║░░░░░
╚█████╔╝  ██████╦╝██║░░██║███████╗███████╗
░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝
"""

#8 BALL IMAGE
#14
#MAIN FUNCTION
def shakeshakeshake():
	#MAIN MENU
	os.system("clear")
	print(title)
	print(f"{m8ballWelcome}")
	question = input("?: ")
	
	#SHAKE SHAKE SHAKE
	count = 1
	for i in range(1,6):
		count += 1
		os.system("clear")
		print(title)
		if (count % 2):			
			print("\n" * i + f"{m8ballWelcome}")
			con = input("Press enter to shake...")
		else:
			print("\033[A" * count + f"{m8ballWelcome}")
			con = input("Press enter to shake...")
				
	randomValue = random.choice(responses)
	words = randomValue.split()
	
	count = 0
	for word in words:
		count += 1
		total = 14
		wordCount = (len(word))
		spaceCount = total - wordCount
		spaceTime = " " * spaceCount	
		string = word.center(14)
		ballAnswer[f"ball{count}"] = string

	#############PRINTING THE BAll#############
	#TOP
	os.system("clear")
	print(title)
	print(m8balltop)
	#MIDDLE
	for i in range(1,6):
		one = ballAnswer[f"startball{i}"]
		two = ballAnswer[f"ball{i}"]
		three = ballAnswer[f"endball{i}"]
		print(one + f"{two}".center(14) + three)
	#BOTTOM	
	print("\033[A" + m8ballbottom)

	print("Would you like to ask another question?")
	while True:
		yesNo = input("[y/n]: ")
		
		if yesNo not in ("y", "n"):
			print("not a valid input...")
			
		elif yesNo == "y":
				shakeshakeshake()
			
		elif yesNo == "n":
			print("Quitting...")
			break

#STARTING THE PLAYTIMES
if __name__=="__main__":
	shakeshakeshake()#w4rm15h
#50 Projects
#15. Magic 8 Ball Game