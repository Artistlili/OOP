class Animal:
    def __init__(self):
        self.__legs = 4

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Woof, woof, woof")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    
    def speak(self):
        print("Meow, meow, meow")


def chorus(Animals):
    for animal in Animals:
        animal.speak()

animals = []
dog1 = Dog()
cat1 = Cat()
animals.append(dog1)
animals.append(cat1)