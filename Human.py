from abc import ABC, abstractmethod


class Human(ABC):

    def __init__(self, gender: str, age: str, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def __str__(self):
        return f"gender: {self.gender}\nage: {self.age}\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\n"