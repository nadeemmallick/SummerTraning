#Take integer input for user he/she presses q, print average and product of all number until user presses q to exit.

numbers = []

while True:
    user_input = input("Enter an integer (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        number = int(user_input)
        numbers.append(number)

    except ValueError:
        print("Invalid input!")

if numbers:
    average = sum(numbers) / len(numbers)
    product = 1

    for num in numbers:
        product *= num

    print("Numbers:", numbers)
    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers entered.")