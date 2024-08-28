class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self) -> str:
        return f"Student ID: {self.id_number} | Student Name: {self.name}"


class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self) -> str:
        return f"{self.name}: {self.department}"

class Course:
    def __init__(self, course_name, course_id, enrolled_students):
        self.course_name = course_name
        self.course_id = course_id

        # List of enrolled students; note that each item would
        # be an instance of the Student class.
        self.enrolled_students = enrolled_students

    def __str__(self) -> str:
        return f"{self.course_id}: {self.course_name}"

    def add_student(self, student):
        self.enrolled_students.append(student)
        self.display_enrolled_students()

    def remove_student(self, student_id):
        # Check if the student exists in the list.
        found_student = False
        student_to_remove = None

        for student in self.enrolled_students:
            if student.id_number == student_id:
                found_student = True
                student_to_remove = student

        if found_student:
            self.enrolled_students.remove(student_to_remove)
        else:
            print(f"Student with id_number {student_id} does not exist.")

        self.display_enrolled_students()

    def display_enrolled_students(self):
        print(f"The list of enrolled students are: {self.enrolled_students}")


class Enrollment:
    def __init__(self, student, course) -> None:
        self.student = student
        self.course = course
        self.grade = None

    def __str__(self) -> str:
        return f"Student: {self.student} -- Grade: {self.grade}"


    def assign_grade(self, grade):
        self.grade = grade



class StudentManagementSystem:

    def __init__(self) -> None:
        self.students = [] # List of students
        self.instructors = [] # List of instructors
        self.enrollments = [] # List of enrollments
        self.courses = [] # List of courses.


    #### ADMISSIONS AND EMPLOYMENTS
    """
    Helper methods to create students and instructors
    """
    def create_student(self, name, id_number, major):
        # Check if the id_number exists already.
        found_student, student = self.find_student(id_number)

        if found_student:
            # A student exists with that id_number
            print("\n\nStudent with the entered id already exists")
            return False, None

        # Create the student
        student = Student(name=name, id_number=id_number, major=major)

        self.add_student(student)
        return True, student

    def create_instructor(self, name, id_number, department):
        # Check if the id_number exists already.
        found_instructor, instructor = self.find_instructor(id_number)

        if found_instructor:
            # A instructor exists with that id_number
            print("\n\nInstructor with the entered id already exists")
            return False, None

        # Create the instructor
        instructor = Instructor(name=name, id_number=id_number, department=department)

        self.add_instructor(instructor)

        return True, instructor

    def create_course(self, course_name, course_id):
        found_course, course = self.find_course(course_id)

        if found_course:
            # A course exists with that id_number
            print("\n\nCourse with the entered id already exists")
            return False, None

        # Create the course
        course = Course(course_name=course_name, course_id=course_id, enrolled_students=[])

        self.add_course(course)

        return True, course

    #### STUDENT METHODS
    def find_student(self, student_id):
        has_found_student = False
        student_obj = None

        for student in self.students:
            if student.id_number == student_id:
                has_found_student = True
                student_obj = student

                return True, student_obj
        return False, None


    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        # Check if the student exists in the list.
        found_student, student_to_remove = self.find_student(student_id)

        if found_student:
            self.students.remove(student_to_remove)
        else:
            print(f"Student with id_number {student_id} does not exist.")

    def update_student(self, student_id, name):
        # Assuming student_id is immutable.
        found_student, student_to_update = self.find_student(student_id)

        if student_to_update is not None:
            # Only run this block of code if the student was found
            self.students.remove(student_to_update) # Remove the item
            student_to_update.name = name # Update the student's name

            # Reassign the student to the list.
            self.students.append(student_to_update)

        else:
            print(f"Student with id_number {student_id} does not exist.")


    ### INSTRUCTOR METHODS
    def find_instructor(self, instructor_id):
        has_found_instructor = False
        instructor_obj = None

        for instructor in self.instructors:
            if instructor.id_number == instructor_id:
                has_found_instructor = True
                instructor_obj = instructor

                return True, instructor_obj
        return False, None

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor_id):
        # Check if the instructor exists in the list.

        found_instructor, instructor_to_remove = self.find_instructor(instructor_id)

        if found_instructor:
            self.instructors.remove(instructor_to_remove)
        else:
            print(f"Student with id_number {instructor_id} does not exist.")

    def update_instructor(self, instructor_id, name):
        # Assuming instructor_id is immutable.
        found_instructor, instructor_to_update = self.find_instructor(instructor_id)

        if instructor_to_update is not None:
            # Only run this block of code if the instructor was found
            self.instructors.remove(instructor_to_update) # Remove the item
            instructor_to_update.name = name # Update the instructor's name

            # Reassign the instructor to the list.
            self.instructors.append(instructor_to_update)

        else:
            print(f"Instructor with id_number {instructor_id} does not exist.")


    ### COURSE METHODS
    def find_course(self, course_id):
        has_found_course = False
        course_obj = None

        for course in self.courses:
            if course.course_id == course_id:
                has_found_course = True
                course_obj = course

                return True, course_obj
        return False, None # No course found with that id

    def add_course(self, course):
        self.courses.append(course)
        return

    def remove_course(self, course_id):
        # Check if the course exists in the list.

        found_course, course_to_remove = self.find_course(course_id)

        if found_course:
            self.courses.remove(course_to_remove)
        else:
            print(f"Course with course_id {course_id} does not exist.")

    def update_course(self, course_id, name):
        # Assuming course_id is immutable.
        found_course, course_to_update = self.find_course(course_id)

        if course_to_update is not None:
            # Only run this block of code if the course was found
            self.courses.remove(course_to_update) # Remove the item
            course_to_update.name = name # Update the course's name

            # Reassign the course to the list.
            self.courses.append(course_to_update)

        else:
            print(f"Course with course_id {course_id} does not exist.")


    ### ENROLLMENT METHODS
    def find_enrollment(self, student_id, course_id):
        has_found_enrollment = False
        enrollment_obj: Enrollment | None = None

        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                has_found_enrollment = True
                enrollment_obj = enrollment

                return True, enrollment_obj
        return False, None # No course found with that id

    def enroll_student(self, student_id, course_id):
        # Check if students and courses exists.
        found_student, student_to_enroll = self.find_student(student_id)

        if not found_student:
            print(f"Student with id: {student_id} not found.")
            return

        found_course, course = self.find_course(course_id)
        if not found_course:
            print(f"Course with id: {course_id} not found.")
            return

        # check if enrollment exists

        found_enrollment, enrollment_obj = self.find_enrollment(student_id, course_id)

        if found_enrollment:
            print("\nStudent has already been enrolled for this course")
            return

        # Create an enrollment object
        enrollment = Enrollment(student=student_to_enroll, course=course)

        # Save that enrollment
        self.enrollments.append(enrollment)
        print("\nEnrollment created successfully.")


    def grade_student(self, student_id, course_id, grade):
        found_student_enrollment, student_enrollment = self.find_enrollment(student_id, course_id)

        if student_enrollment is not None:
            student_enrollment.assign_grade(grade)

        else:
            print("Student enrollment for this course does not exist.")


    def list_students_per_course(self, course_id):
        found_students = []

        for enrollment in self.enrollments:
            if enrollment.course.course_id == course_id:
                found_students.append(enrollment.student)
        return found_students

    def list_courses_per_students(self, student_id):
        found_courses = []

        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id:
                found_courses.append(enrollment.course)
        return found_courses


def main():
    # Run the SystemManagement loop

    user_input = ""

    # Initialize objects
    management_system = StudentManagementSystem()


    while user_input != "exit":

        print(
            """
            1. List Students
            2. Add Student
            3. List Courses
            4. Add Course
            5. View Enrollments
            6. Enroll Student
            """
        )

        user_input = input("What would you like to do? :")

        if user_input == "1":
            # List students
            if len(management_system.students) == 0:
                print("No students found.")
            else:

                for student in management_system.students:
                    print(f"{student}")

        elif user_input == "2":
            student_name = input("Enter student name: ")
            student_id = input("Enter student id (note: id must be unique): ")
            major = input("Enter student major: ")

            created, obj = management_system.create_student(name=student_name, id_number=student_id, major=major)

            if created:
                print("\n\nStudent created successfully.")


        elif user_input == "3":
            if len(management_system.courses) == 0:
                print("No courses found.")
            else:

                for course in management_system.courses:
                    print(f"{course}")

        elif user_input == "4":
            course_name = input("Enter course name: ")
            course_id = input("Enter course id: ")

            created, obj = management_system.create_course(course_name, course_id)

            if created:
                print("\n\n Course created successfully.")

        elif user_input == "5":
            if len(management_system.enrollments) == 0:
                print("No enrollments found.")
            else:

                for enrollment in management_system.enrollments:
                    print(f"{enrollment}")

        elif user_input == "6":
            student_id = input("Enter student id: ")
            course_id = input("Enter course id: ")

            management_system.enroll_student(student_id, course_id)

        else:
            if user_input != "exit":
                print("Invalid input. Please select one of the options below, or type 'exit' to quit.")
            else:
                print("\nGoodbye...")
if __name__ == "__main__":
    main()
