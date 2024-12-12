class Student:
    def __init__(self, name, age, math, science, english):
        self.name = name
        self.age = age
        self.math = math
        self.science = science
        self.english = english

    def get_info(self):
        return f"{self.name}, {self.age}, Math: {self.math}, Science: {self.science}, English: {self.english}"

    def average(self):
        return (self.math + self.science + self.english) / 3

class StudentList:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def remove(self, name):
        self.students = [s for s in self.students if s.name != name]

    def display(self):
        for student in self.students:
            print(f"{student.get_info()} - Average: {student.average():.2f}")

def main():
    student_list = StudentList()

    while True:
        action = input("Do you want to add or remove a student? (add/remove/exit): ").strip().lower()
        
        if action == 'add':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            math = float(input("Enter Math score: "))
            science = float(input("Enter Science score: "))
            english = float(input("Enter English score: "))
            student_list.add(Student(name, age, math, science, english))
            student_list.display()
        elif action == 'remove':
            name = input("Enter name to remove: ")
            student_list.remove(name)
            student_list.display()
        elif action == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Please answer with 'add', 'remove', or 'exit'.")
main()