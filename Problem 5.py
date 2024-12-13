class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.enrolled_students = []

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Enrolled Students: {', '.join(self.enrolled_students) if self.enrolled_students else 'None'}"

def add_course(courses):
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append(Course(course_id, name))
    print("Course added successfully!")

def enroll_student(courses):
    course_id = input("Enter course ID: ")
    student_name = input("Enter student name: ")
    for course in courses:
        if course.course_id == course_id:
            course.enrolled_students.append(student_name)
            print("Student enrolled successfully!")
            return
    print("Course not found!")

def display_courses(courses):
    if not courses:
        print("No courses available.")
    else:
        for course in courses:
            print(course)

def display_enrolled_students(courses):
    course_id = input("Enter course ID to see enrolled students: ")
    for course in courses:
        if course.course_id == course_id:
            if course.enrolled_students:
                print(f"Enrolled students in {course.name}: {', '.join(course.enrolled_students)}")
            else:
                print(f"No students enrolled in {course.name}.")
            return
    print("Course not found!")

def main():
    courses = []
    while True:
        print("\nCourse Enrollment Menu:")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Display Courses")
        print("4. Display Enrolled Students")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_course(courses)
        elif choice == '2':
            enroll_student(courses)
        elif choice == '3':
            display_courses(courses)
        elif choice == '4':
            display_enrolled_students(courses)
        else:
            print("Invalid option. Please try again.")

main()