class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with sample data
if __name__ == "__main__":
    students = [
        Student("Alice", "A101", 3.9),
        Student("Bob", "B202", 3.7),
        Student("Charlie", "C303", 3.5),
        Student("David", "D404", 3.8),
    ]

    sorted_students = sort_students(students)

    print("Sorted Students by CGPA (Descending Order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
