#99059050, Sam Fortuin

#import time for exit delays
import time

#types of cheese, not used in code anywhere
cheeseTypes = ["Emmentaler", "Leerdammer", "Parmigiano Reggiano", "Gouda", "Blue De Rochbaron", "Camambert" "Fourme d'Ambert", "Mozarella"]

#first question
yellowCheese = input("Is the cheese yellow?\n")
yellowCheese = yellowCheese.lower()

#cheese is yellow
if yellowCheese == "y" or yellowCheese == "yes":
    holes = input("does the cheese have holes?\n")
    holes = holes.lower()
    if holes == "y" or holes == "yes":
        expensive = input("Is the cheese way too expensive?\n")
        expensive = expensive.lower()
        if expensive == "y" or expensive == "yes":
            print("The cheese you're thinking of is Emmentaler")
            time.sleep(0.5)
            exit()
        elif expensive == "n" or expensive == "no":
            print("The cheese you're thinking of is Leerdammer")
            time.sleep(0.2)
            exit()
        else:
            print("Input not regonized. Exiting program")
            time.sleep(0.2)
            exit()
    elif holes == "n" or holes == "no":
        rockHard = input("Is the cheese hard as rock?\n")
        rockHard = rockHard.lower()
        if rockHard == "y" or rockHard == "yes":
            print("The cheese you're thinking of is Parmigiano Reggiano")
            time.sleep(0.2)
            exit()
        elif rockHard == "n" or rockHard == "no":
            print("The cheese you're thinking of is Gouda")
            time.sleep(0.2)
            exit()
        else:
            print("Input not regonized. Exiting program")
            time.sleep(0.2)
            exit()
    else:
        print("Input not regonized. Exiting program")
        time.sleep(0.2)
        exit()
#cheese is not yellow
elif yellowCheese == "n" or yellowCheese == "no":
    #is the cheese blue
    blueMold = input("Is the cheese blue?\n")
    blueMold = blueMold.lower()
    if blueMold == "y" or blueMold == "yes":
        #does the bluecheese have a crust
        blueCrust = input("Does the bluecheese have a crust?\n")
        blueCrust = blueCrust.lower()
        #blue has crust
        if blueCrust == "y" or blueCrust == "yes":
            print("The cheese you're thinking off is Blue De Rochbaron")
            time.sleep(0.5)
            exit()
        #non blue has crust
        elif blueCrust == "n" or blueCrust == "no":
            print("The cheese you're thinking off is Fourme d'Ambert")
            time.sleep(0.5)
            exit()
        #else for wacko input
        else:
            print("Input not regonized. Exiting program")
            time.sleep(0.2)
            exit()
    elif blueMold == "n" or blueMold == "no":
        #does the non blue cheese have a crust
        nonBlueCrust = input("Does the cheese have a crust?\n")
        nonBlueCrust = nonBlueCrust.lower()
        if nonBlueCrust == "y" or nonBlueCrust == "yes":
            #non blue cheese has crust
            print("The cheese you're thinking of is Camambert")
            time.sleep(0.5)
            exit()
        elif nonBlueCrust == "n" or nonBlueCrust == "no":
            #non blue cheese deosn't have a crust
            print("The cheese you're thinking of is Mozarella")
            time.sleep(0.5)
            exit()
        else:
            print("Input not regonized. Exiting program")
            time.sleep(0.2)
            exit() 
    else:
        #no valid input
        print("Input not regonized. Exiting program")
        time.sleep(0.2)
        exit()
else:
    #no valid input
    print("Input not regonized. Exiting program")
    time.sleep(0.2)
    exit()