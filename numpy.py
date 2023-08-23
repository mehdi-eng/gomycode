import numpy as np

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Initialize a matrix to store student marks
marks_matrix = np.zeros((num_students, num_subjects))

# Input marks for each student and subject
for i in range(num_students):
    print(f"Enter marks for student {i + 1}:")
    for j in range(num_subjects):
        marks_matrix[i][j] = float(input(f"Subject {j + 1}: "))

# Calculate total marks, percentage, and grade for each student
total_marks = np.sum(marks_matrix, axis=1)
percentages = (total_marks / (num_subjects * 100)) * 100
grades = np.array([calculate_grade(percentage) for percentage in percentages])

# Display results in a tabular format
print("\nStudent\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"{i + 1}\t{total_marks[i]}\t\t{percentages[i]:.2f}%\t\t{grades[i]}")
