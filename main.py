from termcolor import colored
import sqlite3
from sqlite3 import Error
import pickle
import random
import time
import os

title_image = """
___  ____ ____  _ ____ ____ ___ ____
|__] |__/ |  |  | |___ |     |  [__
|    |  \ |__| _| |___ |___  |  ___]
"""

#STORAGE
class vars():
	count = 0
	completed_projects = []
	total_completed = 0
	projects = {}
	options = [1, 2, 3]
	current = "No project"

def Print(text, color):
	print(colored(f"{text}".center(37), f'{color}'))
	
#CREATING CONNECTION TO THE DATABASE
def createConnection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)	
	except Error as e:
		print(e)	
	return conn

def createProject(name):
	number = vars.total_completed + 1
	fileName = f"{number}. {name}"
	os.mkdir(fileName)
	time.sleep(0.1)
	with open(f"{fileName}/main.py", "w") as file:
		file.write(f"#w4rm15h\n#50 Projects\n#{name}")

def clear():
	os.system("clear")
	tc = vars.total_completed
	print(colored(title_image, 'green'))
	print(colored(f"<--====--Completed projects--====-->",'cyan'))
	print(colored(f"--[{tc}]--".center(37), 'green'))
	print()
	print(colored("--=-=--".center(37), 'cyan'))

def yesNo():
	print()
	choice = input(colored("             [y/n]: ", 'cyan'))
	while True:
		if choice not in ("y", "n"):
			print(colored("Try that one again...", 'red'))
		else:
			if choice == "y":
				return("y")
			if choice == "n":
				return("n")

def completeTask(conn, np):
	cur = conn.cursor()
	clear()
	print(colored(f"Did you complete".center(37), "cyan"))
	print()
	print(colored(f"{vars.current}?".center(37), 'green'))
	comp = yesNo()
	if comp == "y":
		sql = f"UPDATE projects SET status = 'Complete' WHERE project='{vars.current}'"
		sql1 = f"UPDATE projects SET status = 'Current' WHERE project='{np}'"
	elif comp == 'n':		
		sql = f"UPDATE projects SET status = 'Incomplete' WHERE project='{vars.current}'"
		sql1 = f"UPDATE projects SET status = 'Current' WHERE project='{np}'"
	try:		
		cur.execute(sql)
		cur.execute(sql1)
		conn.commit()
		projectNo = 1 + vars.total_completed
		print()
		mainMenu()
	except Error as e:
		print(e)
	
def currentTask(conn):
	#CONNECTING TO DB
	cur = conn.cursor()
	current = cur.execute("SELECT project, status FROM projects WHERE status='Current'")
	if not current:
		vars.current = "None"
		return("No Project")
	else:
		p, s = current.fetchone()
		vars.current = p
		return(p)

def completedProjects(conn):
	vars.total_completed = 0
	cur = conn.cursor()
	projects = cur.execute("SELECT project, status FROM projects")
	for project, status in projects:
		if status == "Complete":
			vars.total_completed += 1
			print(colored(f"{project}".center(37), 'green'))

#RANDOM PROJECT SELCTION FUNCTION -- COMPLETE
def randomProject(conn):
	clear()
	cur = conn.cursor()
	selectRandom = cur.execute("SELECT project, status FROM projects ORDER BY RANDOM() LIMIT 1;")
	np, s = selectRandom.fetchone()
	print()
	print(colored(f"How about".center(37), 'cyan'))
	print()
	print(colored(f"{np}?".center(37), 'green'))
	choice = yesNo()
	if choice == "y":
		completeTask(conn, np)
	elif choice == "n":
		randomProject(conn)
	
#MAIN MENU FUNCTION -- COMPLETE
def mainMenu():
	#LOADING AND REFRESHING DATA
	# SCREEN
	clear()
	#DATABASE
	database = "50projects.db"
	conn = createConnection(database)
	#CURRENT
	Print("=- C U R R E N T -=", 'cyan')
	current = currentTask(conn)
	print(colored(f"{current}".center(37), 'green'))
	print()
	#COMPLETE	
	Print("=C O M P L E T E D=", 'cyan')
	completedProjects(conn)
	print(colored("--=-=--".center(37), 'cyan'))
	print()
	#MAIN MENU
	print()
	print(colored("-===- M E N U -===-".center(37), 'green'))
	print(colored("--=-=--".center(37), 'cyan'))
	print(colored("1. Gimme a project!  ".center(37), 'green'))
	print(colored("2. Choose a project  ".center(37), 'cyan'))
	print(colored("3. Complete a project".center(37), 'green'))
	print(colored("4. refresh           ".center(37), 'cyan'))
	print(colored("5. Exit              ".center(37), 'green'))
	print(colored("--=-=--".center(37), 'cyan'))
	#MENU FUNCTIONS
	while True:
		choice = input(colored("        $~ ", 'green'))
		if choice not in ("1", "2", "3", "4", "5", "wipe"):
			print("       C'mon man!")	
		else:
			if choice == "1":
				randomProject(conn)
	
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
#INIT THE FUNCTION
if __name__ == "__main__":
	mainMenu()