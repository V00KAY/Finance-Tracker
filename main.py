import json
import os
import time
from data import data

os.system("cls")

# Functions
def status():

    # Printing and value data collection
    earnings = 0
    for one_key, one_value in data["earnings"].items():
        earnings += one_value
        print(f"{one_key} : {one_value} Kč")
    expenses = data["expenses"]

    # Print currect status
    os.system("cls")
    print(f"\n---\nTotal earnings: {earnings} Kč\nTotal expenses: {expenses} Kč\n---\nStatus = {earnings-expenses} Kč\n---")
    x = input("<Ent>")
    os.system("cls")

def review():
    os.system("cls")

    lets_continue1 = True
    while lets_continue1:
        summary = 0
        investion = 0

        # Printing and value data collection
        print("---")
        for one_key, one_value in data["revision"]["free funds"].items():
            summary += int(one_value)
            print(f"{one_key} : {one_value} Kč")
        for one_key, one_value in data["revision"]["investions"].items():
            summary += int(one_value)
            investion += int(one_value)
            print(f"{one_key} : {one_value} Kč")

        # Error checking
        try:
            percent = investion / (summary / 100)
        except ZeroDivisionError:
            percent = 0

        # Print current review
        print("---")
        print(f"Total balance: {summary} Kč")
        print(f"Of which investment: {investion} Kč or {round(percent, 1)} %")
        print("---")

        # Finding out if user wants to change value and changing value
        AorN = input("Change value (a/n)?  ")
        if AorN == "n":
            lets_continue1 = False
        else:
            change = input("Enter what you want to change: ")
            set_to = int(input("\nEnter the amount: "))
            
            found = False
            for category in data["revision"]:
                if change in data["revision"][category]:
                    data["revision"][category][change] = set_to
                    found = True
                    break
            
            if found == False:
                print(f"Error: Item '{change}' not found.")
                time.sleep(2)



        os.system("cls")

def expenses():
    os.system("cls")

    # Finding out how much user wants to increase or reduce value
    how_much = int(input("\nEnter the amount: "))
    data["expenses"] += how_much
    os.system("cls")

    # Print total expenses
    print(f"\n---\nTotal expenses: {data["expenses"]} Kč\n---")
    x = input("<Ent>")
    os.system("cls")

def earnings():
    os.system("cls")

    # Printing and value data collection
    summary = 0
    print("---")
    for one_key, one_value in data["earnings"].items():
        summary += one_value
        print(f"{one_key} : {one_value} Kč")

    print("---")
    print(f"Total earnings: {summary} Kč")
    print("---")

    # Finding out if user wants to increase or reduce value
    AorN = input("Change value (a/n)?  ")
    if AorN == "n":
        pass
    else:
        change = input("Enter what you want to change: ")
        set_to = int(input("\nEnter the amount: "))
        data["earnings"][change] = data["earnings"][change] + set_to
    os.system("cls")

# The user chooses which file to open
pick_year = input("\nWhich year do you want to open?\nResponse: ")
pick_month = input("\nWhich month do you want to open?\nResponse: ").lower()

# If folder doesnt exist program creates it
folder_path = f"years/{pick_year}"
os.makedirs(folder_path, exist_ok=True)

# Save way to file
way_to_file = f"years/{pick_year}/{pick_month}"

# Verifying the existence of a file and possibly creating it + adding content
if os.path.exists(way_to_file):
    pass
else:
    with open(way_to_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file)
    print("\n---\nNew file created\n---")

    time.sleep(1)
os.system("cls")

# Opening a file and saving data for work
with open(way_to_file, mode="r", encoding="utf-8") as file:
    data = json.load(file)

# Cycle
lets_continue = True
while lets_continue:

    # Prints options
    print("\nWhat do you want to do?\n\n(1) Add earnings\n(2) Add expenses\n(3) Show current status\n(4) Add monthly review\n(5) Exit")

    # Triggering a action
    way = int(input("\nResponse: "))
    if way == 5:
        lets_continue = False

    elif way == 4:
        review()

    elif way == 3:
        status()
        
    elif way == 2:
        expenses()

    elif way == 1:
        earnings()


# Closing a file and saving data after work
with open(way_to_file, mode="w", encoding="utf-8") as file:
    json.dump(data, file)
os.system("cls")
