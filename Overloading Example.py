class Example:
    def __init__ (self, examplename = 'Generic Name'):
        self.examplename = examplename
    def greet (self, name = None):
        if name: 
            print('Hello', name)
        else:
            print('Hello there')

obj = Example('john')
obj.greet()
obj.greet('john')