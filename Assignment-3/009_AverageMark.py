import pandas as pd

data = {
    'student_ID': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva', 'Frank', 'Grace'],
    'gender': ['F', 'M', 'M', 'F', 'F', 'M', 'F'],
    'math': [85, 67, 90, 78, 92, 58, 73],
    'science': [88, 72, 94, 74, 91, 60, 77],
    'english': [90, 65, 88, 82, 85, 70, 79],
    'attendance (%)': [96, 82, 89, 94, 99, 76, 88]
}

df = pd.DataFrame(data)

df['TOTAL'] = df['math']+df['science']+df['english']

df['AVERAGE'] = df['TOTAL']/3

print(df[['name', 'math', 'science', 'english', 'TOTAL', 'AVERAGE']])