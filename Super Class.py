class Student:
    def __init__ (self, name, dob, mark):
        self.__name = name
        self.__dob = dob
        self.__mark = mark

    def displayMark(self):
        print(f"{self.__name}: {self.__mark}")

class fullTimeStudent(Student):
    def __init__ (self, name, dob, mark):
        super().__init__(name, dob, mark)
        super().displayMark()

class partTimeStudent(Student):
    def __init__ (self, name, dob, mark):
        super().__init__(name, dob, mark)
        super().displayMark()

fts = fullTimeStudent("Alice", "2005-04-12", 85)
pts = partTimeStudent("Boo", "2005-04-12", 93)
