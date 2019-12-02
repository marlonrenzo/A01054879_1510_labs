class Student:
    def __init__(self, first, middle, last, student_number):
        self.first = first
        self.middle = middle
        self.last = last
        self.student_number = student_number
        self.courses = {}

    def get_information(self):
        return [f"{self.first} {self.last}", self.student_number, self.get_gpa()]  # return a list of information

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
    cst_student_one = Student("Nicole", "Page", "Brooks", "A00123456")
    cst_student_one.add_course("Comp 1510", 95)
    cst_student_one.add_course("Comp 1113", 87)
    cst_student_one.add_course("Comp 1536", 94)
    print(f"{cst_student_one.first}'s GPA is {cst_student_one.get_gpa()}")

    cst_student_two = Student("Cornelius", "", "Smith", "A00987654")
    cst_student_two.add_course("Comp 1116", 45)
    cst_student_two.add_course("Comp 1930", 65)
    cst_student_two.add_course("Comp 1712", 75)
    print(f"{cst_student_two.first}'s GPA is {cst_student_two.get_gpa()}")


if __name__ == '__main__':
    main()
