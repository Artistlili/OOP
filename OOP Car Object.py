class Car:
    def __init__(self, registration, make):
        self.__registration = registration #string
        self.__make = make #string
        self.__mileage = 0 #integer
        self.__date = '' #string

    def getMake(self):
        return self.__make
    
    def getRegistration(self):
        return self.__registration
    
    def setMileage(self, miles):
        self.__mileage = miles
        return self.__mileage
    
    def setDate(self, Date):
        self.__date = Date
        return self.__date
    
car1 = Car('ABC123', 'Ferrari')
miles = car1.setMileage(45)
date = car1.setDate('12.05.12')
make = car1.getMake()
reg = car1.getRegistration()
print(miles)
print(date)
print(make)
print(reg)