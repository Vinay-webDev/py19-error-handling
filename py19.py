numbers = []
total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        number = float(user_input)
        numbers.append(number)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

if count > 0:
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)

    print("\nResults:")
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
else:
    print("No valid numbers entered.") 
