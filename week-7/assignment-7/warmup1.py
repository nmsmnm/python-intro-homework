with open("../data/notes.txt", "r") as f:
    for number, line in enumerate(f, start=1):
        print(f"Line {number}: {line.strip()}")