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

def loadingProjects():  
    #LOADING FROM DB
    with open("50.w4rm15h", "rb") as p:
        vars.projects = pickle.load(p)
        
    #SORTING THE LIST
    for k, s in vars.projects.items():
        if s == "Complete":
            vars.total_completed += 1
            vars.completed_projects.append(f"{k}")
        elif s == "Current":
            vars.current = f"{k}"

def randomProject():
    p = random.choice(list(vars.projects.keys()))
    print("Alright, the project for tonight is...")
    print(p)
    print("Shall we get cracking?")
    while True:
        choice = input("[y,n]: ")
        if choice not in ("y", "n"):
            print("Try that one again...")
        else:
            if choice == "n":
                randomProjects()
            else:
                vars.projects[f"{p}"] = "Current"
                with open("50.w4rm15h", "wb") as p:
                    pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)
                mainMenu()

    

def completeProject():
    print("Which project are knocking off the list")
    for i in vars.projects:
        print(i)
        
    choice = input("> ")
    if choice not in vars.projects:
        print("not a valid choice")
        mainMenu()
    else:
        vars.projects[f"{choice}"] = "Complete"
        
        with open("50.w4rm15h", "wb") as p:
            pickle.dump(vars.projects, p, pickle.HIGHEST_PROTOCOL)
        mainMenu()

def mainMenu():
    #Loading pickle
    loadingProjects()
    #menu
    os.system("clear")
    print(title_image)
    print(f"---==--Completed-projects=[{vars.total_completed}]--==---\n")
    print(f"Current: {vars.current}")
    for i in vars.completed_projects:
        print(f"Complete: {i}")
    #options
    print("-------------------")
    print("1. Gimme a project!")
    print("2. Complete a project")
    print("3. Refresh")
    print("-------------------")
    #Input for menu
    while True:
        choice = input("> ")
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