class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing..")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am a employee and I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print("No salary for programmer")

p = Person()
p.takeBreath()
# print(p.company)  throws error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)