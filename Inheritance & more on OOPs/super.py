# Super() method:-

#Super method is used to access the methods of a super/ parent class in the derived class.

class Person:
    country = "India"
    def __init__(self):
        print("Initializing Person..\n")

    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee..\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath() # Super() method
        print("I am a employee and I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer..\n")

    def getSalary(self):
        print("No salary for programmer")

    def takeBreath(self):
        super().takeBreath() # Super() method
        print("I am a programmer and I am luckily breathing++..")

# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()

