from termcolor import colored
import time
import pickle
import random
import os

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

#LOADING THE PROJECTS
def loadingProjects():  
    #LOADING FROM DB
    with open("50.w4rm15h", "rb") as p:
        vars.projects = pickle.load(p)       
    #SORTING THE LIST
    for k, s in vars.projects.items():       
        if s == "Complete" and k not in vars.completed_projects:
            vars.total_completed += 1
            vars.completed_projects.append(f"{k}")
        elif s == "Current":
            vars.current = f"{k}"
          
#CHOOSING A RANDOM PROJECT
def randomProject():
    p = random.choice(list(vars.projects.keys()))
    os.system("clear")
    print("Alright, the project for tonight is...\n")
    print(p)
    print("Shall we get cracking sir?")
    while True:
        choice = input("[y,n]: ")
        if choice not in ("y", "n"):
            print(colored("Try that one again...", 'red'))
        else:
            if choice == "n":
                randomProjects()
                
            if choice == "y":
                for k, s in vars.projects.items():
                    if s == "Current":
                        while True:
                            print(colored(f"do you want to complete {k}?", 'yellow'))
                            choice1 = input("[y,n]: ")
                            if choice1 not in ("y", "n"):
                                print(colored("Try that one again...", 'red'))
                            else:
                                if choice1 == 'y':
                                    s = "Complete"
                                    print(p)
                                    break
                                if choice1 == "n":
                                    s = "Incomplete"
                                    print(p)
                                    break
                                                                     
                vars.projects[f"{p}"] = "Current"
                with open("50.w4rm15h", "wb") as z:
                    pickle.dump(vars.projects, z, pickle.HIGHEST_PROTOCOL)
                mainMenu()
                
#COMPLETING AN ORDER
def completeProject():
    print("\n")
    print("Which project are knocking off the list")
    for i, s in vars.projects.items():
        print(i + ": " + s)
        
    choice = input("> ")
    if choice not in vars.projects:
        print("not a valid choice")
        mainMenu()
    else:
        vars.projects[f"{choice}"] = "Complete"
        
        with open("50.w4rm15h", "wb") as p:
            pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)
        mainMenu()
        
#MAIN MENU AND DISPLAY
def mainMenu():
    #Loading pickle
    loadingProjects()
    
    #menu
    os.system("clear")
    print(title_image)
    print(colored(f"--===--Completed-projects=[{vars.total_completed}]--===--\n", 'green'))
    print("=- C U R R E N T -=")
    print(colored(f". {vars.current}", 'yellow'))   
    print("\n=C O M P L E T E D=\n")
    for i in vars.completed_projects:
        print(colored(f". {i}", 'green'))
        
    #options
    print("-===- M E N U -===-\n")
    print("1. Gimme a project!")
    print("2. Complete a project")
    print("3. Refresh")
    print("--===--")
    
    #Input for menu
    while True:
        choice = input("[1,2,3]: ")
        if choice not in ("1", "2", "3"):
            print("C'mon man!")
            
        else:
            if choice == "1":
                randomProject()

            if choice == "2":
                completeProject()

            if choice == "3":
                mainMenu()

if __name__ == "__main__":
    mainMenu()

#-----------storage------------

# with open("list.txt", "r") as l:
#     for line in l:
#         nl = line.replace("\n", "")
#         vars.projects[f"{nl}"] = "Incomplete"

# with open("50.w4rm15h", "wb") as p:
#     pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)

# with open("50.w4rm15h", "rb") as p:
#     vars.projects = pickle.load(p)