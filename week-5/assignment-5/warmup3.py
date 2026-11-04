names = ["Anna", "David", "Sara", "Marcus", "Emma"]

search_name = input("Enter a name to search for: ")

found = False

for i in range(len(names)):
    if names[i] == search_name:
        print("Found", search_name, "at index", i)
        found = True
        break

if not found:
    print(search_name, "was not found in the list.")