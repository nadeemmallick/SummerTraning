import pandas as pd

data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva', 'Frank', 'Grace'],
    'Gender': ['F', 'M', 'M', 'F', 'F', 'M', 'F'],
    'Math': [85, 67, 90, 78, 92, 58, 73],
    'Science': [88, 72, 94, 74, 91, 60, 77],
    'English': [90, 65, 88, 82, 85, 70, 79],
    'Attendance (%)': [96, 82, 89, 94, 99, 76, 88]
}

df = pd.DataFrame(data)

df['TOTAL'] = df['Math'] + df['Science'] + df['English']
df['Average'] = df['TOTAL']/3

df['Grade'] = df['Average'].apply(lambda avg: 'A' if avg >= 85 else ('B' if avg >= 70 else 'C'))

print(df[['Name', 'Math', 'Science', 'English', 'Average', 'Grade']])