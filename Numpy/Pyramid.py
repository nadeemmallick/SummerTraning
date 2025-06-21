def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

pyramid_pattern = int(input("Enter the number you wanted:"))
