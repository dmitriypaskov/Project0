import Human


class Student(Human.Human):

    def __init__(self, gender: str, age: str, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    # def __eq__(self, other):
    #     if isinstance(other, Student):
    #         return self.__str__() == other.__str__()

    def __str__(self):
        return f"{super().__str__()}record_book: {self.record_book}\n\n"
