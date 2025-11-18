import json
import os
import time

os.system("cls")

data = {
    "earnings": 0,
    "expenses": 0,
    "revision": {
        "investions": {
            "Revolut Robo": 0,
            "Investown": 0,
            "Fingood": 0,
            "Investicni predmety": 0,
            "Investicni listky": 0
        },
        "free funds": {
            "Airbank": 0,
            "Revolut Finance": 0,
            "Stovkomat": 0,
            "Hotovost": 0
        }
    }
}

pick_year = input("\nWhich year do you want to open?\nOdpověd: ")
pick_month = input("\nWhich month do you want to open?\nOdpověd: ").lower()
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

    print("\nWhat do you want to do??\n\n(1) Add earnings\n(2) Add expenses\n(3) Show current status\n(4) Add monthly review\n(5) Exit")
    way = int(input("\nOdpověd: "))

    if way == 5:
        lets_continue = False
    elif way == 3:
        earnings = data["earnings"]
        expenses = data["expenses"]

        os.system("cls")
        print(f"\n---\nTotal earnings: {earnings} Kč\nTotal expenses: {expenses} Kč\n---\nStatus = {earnings-expenses} Kč\n---")
        x = input("<Ent>")
        os.system("cls")

    elif way == 4:
        os.system("cls")

        lets_continue1 = True
        while lets_continue1:
            summary = 0
            investion = 0
            print("---")

            for one_key, one_value in data["revision"]["free funds"].items():
                summary += int(one_value)
                print(f"{one_key} : {one_value} Kč")
            for one_key, one_value in data["revision"]["investions"].items():
                summary += int(one_value)
                investion += int(one_value)
                print(f"{one_key} : {one_value} Kč")

            percent = round(investion/(summary/100), 1)
            print("---")
            print(f"Total balance: {summary} Kč")
            print(f"Of which investment: {investion} Kč or {percent} %")
            print("---")


            AorN = input("Change value (a/n)?  ")
            if AorN == "n":
                lets_continue1 = False
            else:
                change = input("Enter what you want to change: ")
                set_to = input("\nEnter the amount: ")
                data["revision"][change] = set_to
            os.system("cls")
        

    elif way == 2:
        os.system("cls")
        how_much = int(input("\nEnter the amount: "))
        data["expenses"] += how_much
        os.system("cls")

        print(f"\n---\nTotal expenses: {data["expenses"]} Kč\n---")
        x = input("<Ent>")
        os.system("cls")

    elif way == 1:
        os.system("cls")
        how_much = int(input("\nEnter the amount: "))
        data["earnings"] += how_much
        os.system("cls")

        print(f"\n---\nTotal earnings: {data["earnings"]} Kč\n---")
        x = input("<Ent>")
        os.system("cls")

# Closing a file and saving data after work
with open(way_to_file, mode="w", encoding="utf-8") as file:
    json.dump(data, file)
os.system("cls")
