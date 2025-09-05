class Animal:
    def __init__(self, s, n):
        self.__state = s
        self.__size = n

    def getState(self):
        return self.__state
    
    def getSize(self):
        return self.__size

    def feed(self):
        self.__size += 1
        if self.__size == 5:
            self._state = "bigFish"

myAnimal = Animal("smallFish", 1)
print(myAnimal.getState(), "is of size", myAnimal.getSize())

while myAnimal.getState() != "bigFish":
    myAnimal.feed()
print("It is now a", myAnimal.getState(), "of size", myAnimal.getSize())
