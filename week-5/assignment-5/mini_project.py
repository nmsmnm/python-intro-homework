numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        smallest = numbers[0]

        for number in numbers:
            if number < smallest:
                smallest = number

        print("Minimum number:", smallest)

    elif choice == "2":
        largest = numbers[0]

        for number in numbers:
            if number > largest:
                largest = number

        print("Maximum number:", largest)

    elif choice == "3":
        try:
            target = int(input("Enter a number to search for: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        found = False

        for i in range(len(numbers)):
            if numbers[i] == target:
                print("Found at index:", i)
                found = True
                break

        if not found:
            print("Number not found.")

    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print("Sorted list:", numbers)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.")