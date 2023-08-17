class Calculator:
    def __init__(self , num):
        self.number = num  # self.number is act as new variable

    def square(self):
        print(f"Square value of {self.number} is {self.number**2}") # (n)^2

    def squareRoot(self):
        print(f"Square root value of {self.number} is {self.number**0.5}") # (n)^(1/2)

    def cube(self):
        print(f"Cube value of {self.number} is {self.number**3}") # (n)^3

    @staticmethod
    def greet():
        print("*********Hello guys, welcome to best calculator**********")


val = Calculator(3)
val.greet()

val.square()
val.cube()
val.squareRoot()

