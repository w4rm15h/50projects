from termcolor import colored
from datetime import datetime
import sqlite3
from sqlite3 import Error
import getpass
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

#CHEECK LITTLE PRINT FUNCTION
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

#CREATING THE FILES AND FOLDERS
def createProject(project):
	os.mkdir(f"{project}")
	time.sleep(0.1)
	with open(f"{project}/main.py", "a") as file:
		file.write(f"#w4rm15h\n#50 Projects\n#{project}")
		
#CLEARING THE SCREEN
def clear(conn):
	os.system("clear")
	cur = conn.cursor()
	completedProjectsTotal = cur.execute("SELECT Count(), rowid FROM projects WHERE status='Complete'")
	tc, rid = completedProjectsTotal.fetchone()
	print(colored(title_image, 'green'))
	print(colored(f"<--====--Completed projects--====-->",'cyan'))
	print(colored(f"--[{tc}]--".center(37), 'green'))
	print()
	print(colored("--=-=--".center(37), 'cyan'))
	vars.total_completed = tc

#YES OR NO OPTION FUNCTION
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
				
#GETTING COMPLETED PROJECTS
def completedProjects(conn):
	vars.total_completed = 0
	cur = conn.cursor()
	projects = cur.execute("SELECT project, status FROM projects")
	for project, status in projects:
		if status == "Complete":
			vars.total_completed += 1
			print(colored(f"{project}".center(37), 'green'))

#COMPLETE A TASK FUNCTION
def completeTask(conn, np):
	cur = conn.cursor()
	clear(conn)
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

#GETTING THE CURRENT TASK
def currentTask(conn):
	cur = conn.cursor()
	try:
		current = cur.execute("SELECT project, status FROM projects WHERE status='Current'")
		p, s = current.fetchone()
		vars.current = p
		return(p)		
	except:
		vars.current = "No Current Project"
		return("No Current Project")

#RANDOM PROJECT ALLOCATION
def randomProject(conn):
	clear(conn)
	cur = conn.cursor()
	selectRandom = cur.execute("SELECT rowid, project, status FROM projects ORDER BY RANDOM() LIMIT 1;")
	rid, np, s = selectRandom.fetchone()
	print()
	print(colored(f"How about".center(37), 'cyan'))
	print()
	print(colored(f"{np}?".center(37), 'green'))
	choice = yesNo()
	if choice == "y":
		createProject(f"{rid}. {np}")
		completeTask(conn, np)
	elif choice == "n":
		randomProject(conn)

#CHOOSING THE PROJECT
def chooseProject(conn):
	clear(conn)
	cur = conn.cursor()
	p = cur.execute("SELECT rowid, project, status FROM projects WHERE status='Incomplete'")
	numbers = []
	for rowid, project, status in p.fetchall():
		numbers.append(f"{rowid}")
		if (rowid % 2):
			print(colored(f"{rowid}. {project}", 'green'))
		else:
			print(colored(f"{rowid}. {project}", 'cyan'))				
	while True:
		choice = input("$~ ")
		if choice not in numbers:
			print("nope")
		else:
			c = cur.execute(f"SELECT rowid, project, status FROM projects WHERE rowid='{choice}'")
			rowid, project, status = c.fetchone()
			clear(conn)
			Print("alright, so...", 'cyan')
			print()
			Print(f"{project}", 'green')
			yn = yesNo()
			if yn == "y":
				createProject(f"{rowid}. {project}")
				completeTask(conn, project)
			else:
				chooseProject(conn)

#RESETTINGS THE LIST
def resettingList(conn):
	clear(conn)
	while True:
		key = getpass.getpass(colored("Enter the Key: ".center(37), 'yellow'))
		if key == os.environ.get("pass"):
			clear(conn)
			cur = conn.cursor()
			reset = cur.execute("UPDATE projects SET status='Incomplete'")
			conn.commit()
			clear(conn)
			Print("Database refreshed, let's get going.", 'green')
			hold = input(colored("Push Enter to continue...".center(37), 'cyan'))
			break
		else:
			Print("Incorrect Password", 'red')

#MAIN MENU FUNCTION
def mainMenu():
	#DATABASE
	database = "50projects.db"
	conn = createConnection(database)
	clear(conn)
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
	print()
	print(colored("1. Gimme a project!  ".center(37), 'cyan'))
	print(colored("2. Choose a project  ".center(37), 'green'))
	print(colored("3. refresh the list  ".center(37), 'cyan'))
	print(colored("4. Exit              ".center(37), 'green'))
	print()
	print(colored("--=-=--".center(37), 'cyan'))
	#MENU FUNCTIONS
	while True:
		choice = input(colored("        $~ ", 'green'))
		if choice not in ("1", "2", "3", "4"):
			print("       C'mon man!")	
		else:
			if choice == "1":
				randomProject(conn)
				break
	
			if choice == "2":
				chooseProject(conn)
				break
	
			if choice == "3":
				resettingList(conn)
				break
	
			if choice == "4":
				exit()
	mainMenu()

#INIT THE FUNCTION
if __name__ == "__main__":
	mainMenu()