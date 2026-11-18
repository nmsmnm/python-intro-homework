import csv
import os
from datetime import datetime

path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(path):
    print("Error: expenses.csv not found.")
    exit()

with open(path, "r") as f:
    expenses = list(csv.DictReader(f))

for expense in expenses:
    expense["amount"] = float(expense["amount"])

food_expenses = []

for expense in expenses:
    if expense["category"] == "Food":
        food_expenses.append(expense)

total = sum(expense["amount"] for expense in food_expenses)

today = datetime.now().strftime("%B %d, %Y")

with open("food_report.txt", "w") as f:
    f.write(f"Food Expense Report — generated {today}\n")

    for expense in food_expenses:
        f.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

    f.write(f"Total: ${total:.2f}\n")

print("Food report created successfully.")