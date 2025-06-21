while True:
    score = int(input("Enter score (0-100): "))
    if 0 <= score <= 100:
        break
    print("Invalid score, try again.")

if score < 40:
    print("Fail")
elif score < 60:
    print("Pass")
elif score < 80:
    print("Merit")
else:
    print("Distinction")