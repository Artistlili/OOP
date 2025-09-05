class Car:
    def __init__(self, reg, make):
        self._registration = reg
        self._make = make
        self._mileage = 0
        self._doi = ""
    
    def getRegistration(self):
        return self._registration
    
    def getMake(self):
        return self._make
    
    def getMileage(self):
        return self._mileage
    
    def getDOI(self):
        return self._doi
    
    def setInspectionData (self, mileage, doi):
        self._mileage = mileage
        self._doi = doi

