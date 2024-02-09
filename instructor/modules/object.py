class Parent:
    def _init_(self, a, b):
        self.number_one = a
        self.number_two = b

    def addition(self):
        return self.number_one + self.number_two

    def substaction(self):
        return self.number_one - self.number_two
    
    def multiplication(self):
        return self.number_one * self.number_two
    
    def division(self):
        return self.number_one / self.number_two
    

class Child(Parent):
    def _init_(self, a, b):
        super()._init_(a, b)
    
    def result(self):
        x = int(input("Enter 1 for Add, 2 for Substract, 3 for Multiply and 4 for Divide: "))
        if x == 1:
            print("Answer is", self.addition())
        elif x == 2:
            print("Answer is", self.substaction())
        elif x == 3:
            print("Answer is", self.multiplication())
        else:
            print("Answer is", self.division())

obj = Child(12,3)
obj.result()