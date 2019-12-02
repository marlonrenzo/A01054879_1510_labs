# James R. and Marlon F. || Lab 12

class Student:

    __students = "A00000000"
    __number = "0"

    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
        self.courses = {}
        self.student_number = Student.__students
        Student.__number = str(int(Student.__number) + 1)  # Move on to next student number
        Student.__students = "A" + ("0" * (8 - len(Student.__number))) + Student.__number  # assign new student number

    def get_information(self):
        return f"{self.first} {self.middle} {self.last}, {self.student_number}, {len(self.courses.keys())} courses, GPA: {self.get_gpa()}"

    def get_gpa(self):
        number_of_courses = 0  # total number of courses taken
        grades = 0  # total grades
        for value in self.courses.values():
            number_of_courses += 1
            grades += value
        return float(f"{grades / number_of_courses:.1f}")  # return a gpa as a float with 1 decimal place

    def change_last_name(self, new_last_name):
        self.last = new_last_name

    def add_course(self, class_name, class_grade):
        self.courses[class_name] = class_grade


def main():
    cst_student_one = Student("Nicole", "Page", "Brooks")
    cst_student_one.add_course("Comp 1510", 95)
    cst_student_one.add_course("Comp 1113", 87)
    cst_student_one.add_course("Comp 1536", 94)

    print(f"{cst_student_one.first}'s GPA is {cst_student_one.get_gpa()}")
    cst_student_one.change_last_name("Wang")
    print(cst_student_one.get_information())

    cst_student_two = Student("Cornelius", "", "Smith")
    cst_student_two.add_course("Comp 1116", 45)
    cst_student_two.add_course("Comp 1930", 65)
    cst_student_two.add_course("Comp 1712", 75)

    print(f"{cst_student_two.first}'s GPA is {cst_student_two.get_gpa()}")
    print(cst_student_two.get_information())


if __name__ == '__main__':
    main()
