class Area:
    def __init__(self, shape = 'Unknown Shape'):
        self.shape = shape
    
    def area(self, side1, side2 = None):
        if side2:
            self.shape = "rectangle"
            print(f"{self.shape} : {side2*side1}")
        else:
            self.shape = "square"
            print(f"{self.shape} : {side1**2}")

obj = Area()
obj.area(5)
obj.area(5,6)