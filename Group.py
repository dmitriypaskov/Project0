import Student
import TooManyStudentsError


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise TooManyStudentsError.TooManyStudentsError()

    def delete_student(self, last_name: str):
        if self.find_student(last_name) in self.group:
            self.group.remove(self.find_student(last_name))

    def find_student(self, last_name: str):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def count(self):
        return len(self.group)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += student.__str__()
        return f'Number:{self.number}\n\n{all_students} '
