class Student:
    def __init__(self, student_id, name, course, grade1, grade2, grade3, grade4):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.grade4 = grade4

    def get_average(self):
        return (self.grade1 + self.grade2 + self.grade3 + self.grade4) / 4

students = []

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))
    grade4 = float(input("Enter grade 4: "))
    student = Student(student_id, name, course, grade1, grade2, grade3, grade4)
    students.append(student)
    print("Student added successfully!")

def update_grade():
    student_id = input("Enter student ID to update grade: ")
    for student in students:
        if student.student_id == student_id:
            grade_num = int(input("Enter grade number to update (1-4): "))
            if grade_num == 1:
                student.grade1 = float(input("Enter new grade 1: "))
            elif grade_num == 2:
                student.grade2 = float(input("Enter new grade 2: "))
            elif grade_num == 3:
                student.grade3 = float(input("Enter new grade 3: "))
            elif grade_num == 4:
                student.grade4 = float(input("Enter new grade 4: "))
            else:
                print("Invalid grade number.")
            print("Grade updated successfully!")
            return
    print("Student not found.")

def display_students():
    if not students:
        print("No students in the system.")
        return
    for student in students:
        print(f"ID: {student.student_id}, Name: {student.name}, Course: {student.course}, Average Grade: {student.get_average():.2f}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Update Grade")
        print("3. Display Students")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            update_grade()
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()