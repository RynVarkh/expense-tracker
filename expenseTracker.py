#add daily expense tracker and store it in json file with time stamp

import json
import os
from datetime import datetime

FILE = "expenses.json"

def add():
    title = input("Title: ")
    amount = float(input("Amount: "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            expense = json.load(f)
    else:
        expense = []

    expense.append({"Title":title , "Amount":amount , "Timestamp":timestamp})

    with open(FILE, "w") as f:
        json.dump(expense, f, indent=4)


def view():
    if not os.path.exists(FILE):
        print("No Histroy Available")
        return
    
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            expense = json.load(f)

        if not expense:
            print("No Expenses")
def main():
    add()


if __name__ == "__main__":
    main()