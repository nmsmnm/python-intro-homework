student = {
    "name": "Nazerke",
    "grade": 90,
    "subjects": ["Python", "Math", "English"]
}

for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print("Updated student:", student)