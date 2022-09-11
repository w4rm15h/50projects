from termcolor import colored
import pickle
import random
import os
import time

title_image = """
___  ____ ____  _ ____ ____ ___ ____ 
|__] |__/ |  |  | |___ |     |  [__  
|    |  \ |__| _| |___ |___  |  ___]
"""

class vars():
	count = 0
	completed_projects = []
	total_completed = 0
	projects = {}
	options = [1, 2, 3]
	current = "No project"

def sneakyReset():
	for k, s in vars.projects.items():
		vars.projects[f"{k}"] = "Incomplete"

	with open("50.w4rm15h", "wb") as z:
		pickle.dump(vars.projects, z, pickle.HIGHEST_PROTOCOL)

def makeList():

	with open("list.txt", 'r', encoding='UTF-8') as file:
		while (line := file.readline().rstrip()):
			print(line)
			vars.projects[line] = "Incomplete"
			
	with open("50.w4rm15h", 'wb') as f:
		pickle.dump(vars.projects, f, pickle.HIGHEST_PROTOCOL)

def clear():
	os.system("clear")
	print(colored(title_image, 'green'))
	print(
		colored(f"--===--Completed-projects=[{vars.total_completed}]--===--\n",
				'green'))

def yesNo():
	choice = input("[y/n]: ")
	while True:
		if choice not in ("y", "n"):
			print(colored("Try that one again...", 'red'))
		else:
			if choice == "y":
				return("y")
			if choice == "n":
				return("n")

def createProject(name):
	number = vars.total_completed + 1
	fileName = f"{number}. {name}"
	os.mkdir(fileName)
	time.sleep(0.1)
	with open(f"{fileName}/main.py", "w") as file:
		file.write(f"#w4rm15h\n#50 Projects\n#{name}")
				
#LOADING THE PROJECTS
def loadingProjects():
	#LOADING THE LIST
	with open("50.w4rm15h", "rb") as p:
		vars.projects = pickle.load(p)

#SORTING THE LIST
	vars.current = "No Project"
	vars.completed_projects.clear()

	for k, s in vars.projects.items():
		if s == "Complete":
			vars.total_completed += 1
			vars.completed_projects.append(f"{k}")
		if s == "Current":
			vars.current = k

def completeCurrent():
	for project in projects:
		

			
#CHOOSING A PROJECT
def chooseProject():
	clear()
	counter = 0
	ql = {}
	print(colored("------------", 'cyan'))
	for project in vars.projects:
		checking = vars.projects[project]
		if checking != "Complete":
			counter += 1
			ql[f"{counter}"] = f"{project}"				
			if (counter % 2) == 0:
				print(colored(f"{counter}. {project}", 'cyan'))
			else:
				print(colored(f"{counter}. {project}", 'green'))

			
	print(colored("------------", 'cyan'))
	choice = input("Enter index number: ")
	listing = ql[choice]
	clear()
	print(listing)
	print("Shall we get cracking sir?")
	choice = yesNo()	
	if choice == "n":
		mainMenu()
	if choice == "y":
		for k, s in vars.projects.items():
			if s == "Current":
				print(colored(f"is {k} complete?",'yellow'))	
				choice1 = yesNo()
				
				if choice1 == "y":
					vars.projects[k] = "Complete"
					
				if choice1 == "n":
					vars.projects[k] = "Incomplete"
									
		vars.projects[listing] = "Current"
		createProject(listing)
		
		with open("50.w4rm15h", "wb") as z:
			pickle.dump(vars.projects, z, pickle.HIGHEST_PROTOCOL)
		mainMenu()

#CHOOSING A RANDOM PROJECT
def randomProject():
	p = random.choice(list(vars.projects.keys()))
	clear()
	print("--===--".center(36))
	print(p)
	print("--===--".center(36))
	print("Shall we get cracking sir?")
	choice = yesNo()	
	if choice == "n":
		randomProject()
	if choice == "y":
		for k, s in vars.projects.items():
			if s == "Current":
				print(colored(f"is {k} complete?",'yellow'))	
				choice1 = yesNo()
				
				if choice1 == "y":
					vars.projects[k] = "Complete"
					
				if choice1 == "n":
					vars.projects[k] = "Incomplete"
									
		vars.projects[p] = "Current"
		createProject(p)
		with open("50.w4rm15h", "wb") as z:
			pickle.dump(vars.projects, z, pickle.HIGHEST_PROTOCOL)
		mainMenu()

#COMPLETING AN ORDER
def completeProject():
	clear()
	counter = 0
	ql = {}
	print(colored("------------", 'cyan'))
	for project in vars.projects:
		checking = vars.projects[project]
		if checking != "Complete":
			counter += 1
			ql[f"{counter}"] = f"{project}"				
			if (counter % 2) == 0:
				print(colored(f"{counter}. {project}", 'cyan'))
			else:
				print(colored(f"{counter}. {project}", 'green'))
			
	print(colored("------------", 'cyan'))
	while True:
		choice = input("Enter index number: ")
		if choice not in ql:
			print("NAH")
		else:
			listing = ql[f"{choice}"]
			vars.projects[listing] = "Complete"
			break

	with open("50.w4rm15h", "wb") as p:
		pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)
		
	mainMenu()

def mainMenu():
	loadingProjects()
	clear()	
	print(colored("=- C U R R E N T -=".center(36), 'cyan'))
	print(colored(f"{vars.current}".center(36), 'green'))
	print(colored("=C O M P L E T E D=".center(36), 'cyan'))
	for i in vars.completed_projects:
		print(colored(f"{i}".center(36), 'green'))
	print()
	print("-===- M E N U -===-".center(36))
	print("1. Gimme a project!  ".center(36))
	print("2. Choose a project  ".center(36))
	print("3. Complete a project".center(36))
	print("4. refresh           ".center(36))
	print("5. Exit              ".center(36))
	print("--===--".center(36))
	#Input for menu
	while True:
		choice = input("       : ")
		if choice not in ("1", "2", "3", "4", "5", "wipe"):
			print("       C'mon man!")
	
		else:
			if choice == "1":
				randomProject()
	
			if choice == "2":
				chooseProject()
	
			if choice == "3":
				completeProject()
	
			if choice == "4":
				mainMenu()
	
			if choice == "5":
				exit()

			if choice == "wipe":
				print("Are you sure you sure you want to wipe and refresh the list?")
				w = yesNo()
				if w == "y":
					sneakyReset()
					print("Database refreshed, reloading main menu")
					time.sleep(1)
					mainMenu()
				else:
					mainMenu()


if __name__ == "__main__":
	mainMenu()
	#makeList()
	#sneakyReset()

#-----------storage------------

# with open("list.txt", "r") as l:
#     for line in l:
#         nl = line.replace("\n", "")
#         vars.projects[f"{nl}"] = "Incomplete"

# with open("50.w4rm15h", "wb") as p:
#     pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)

# with open("50.w4rm15h", "rb") as p:
#     vars.projects = pickle.load(p)

# choice = input("[y,n]: ")
# if choice not in ("y", "n"):
# 	print(colored("Try that one again...", 'red'))
