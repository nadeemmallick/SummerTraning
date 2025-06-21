n = int(input("Enter number of employees: "))
employees = []
for _ in range(n):
    name = input("Name: ")
    dept = input("Department: ")
    salary = int(input("Salary: "))
    employees.append({'name': name, 'department': dept, 'salary': salary})

employees.sort(key=lambda x: x['salary'], reverse=True)
print("\nSorted Employees by Salary:")
for emp in employees:
    print(emp)

print("\nDepartment of highest paid employee:", employees[0]['department'])