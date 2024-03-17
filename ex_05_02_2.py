numbers = []

while True:
    user_input = input("Enter a number or 'done' to finish: ")

    if user_input == 'done':
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a numberic value or 'done' to continue")

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
        print("No numbers were entered.")