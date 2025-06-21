marks = list(map(int, input("Enter marks separated by space: ").split()))
avg = sum(marks) / len(marks)
high = max(marks)
low = min(marks)
above_avg = len([m for m in marks if m > avg])

print(f"Average: {avg:.2f}\nHighest: {high}\nLowest: {low}\nStudents above average: {above_avg}")