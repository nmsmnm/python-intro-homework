def is_valid_score(score):
    return type(score) is int and 0 <= score <= 100


score = int(input("Enter your score: "))

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")