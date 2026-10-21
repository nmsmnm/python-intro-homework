# Mini Project - Day Planner

day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "monday":
    if time == "morning":
        print("Suggestion: Go to the gym!")
    elif time == "afternoon":
        print("Suggestion: Study Python.")
    elif time == "evening":
        print("Suggestion: Watch a movie.")

elif day == "tuesday":
    if time == "morning":
        print("Suggestion: Have a nice breakfast.")
    elif time == "afternoon":
        print("Suggestion: Do your homework.")
    elif time == "evening":
        print("Suggestion: Go for a walk.")

elif day == "wednesday":
    if time == "morning":
        print("Suggestion: Drink coffee and read.")
    elif time == "afternoon":
        print("Suggestion: Practice coding.")
    elif time == "evening":
        print("Suggestion: Cook dinner.")

elif day not in ["monday", "tuesday", "wednesday"]:
    print("Sorry, I don't recognize that day.")
    exit()

if time not in ["morning", "afternoon", "evening"]:
    print("Sorry, I don't recognize that time.")