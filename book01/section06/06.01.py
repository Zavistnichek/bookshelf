num_students = int(input("Enter the number of students: "))
students = {}

for _ in range(num_students):
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")
    students[name] = grade

print("\nDictionary of students and their grades:")
print(students)
