import os

print(os.getcwd())

path = os.path.join("..", "data", "expenses.csv")

if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print(path)