class Engine:
    def __init__(self, horsepower):
        self.__horsepower = horsepower #DECLARE horsepower: INTERGER
    
    def getHorsePower(self):
        return self.__horsepower
    

class Car:
    def __init__(self, brand, horsepower):
        self.__brand = brand #DECLARE brand: STRING
        self.engine = Engine(horsepower) #DECLARE enging: ENGINE
    
    def getBrand(self):
        return self.__brand
    
    def spec(self):
        print (f"{self.getBrand()} with {self.engine.getHorsePower()} HP")

mycar = Car("Toyota", "150")
mycar.spec()