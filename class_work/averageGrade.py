def average(grades):
    if len(grades) == 0:
        return 0  
    total = sum(grades)
    average = total / len(grades)
    return average

grades = [85, 90, 78, 92, 88]
avg = average(grades)
print("Average Grade:",avg )
