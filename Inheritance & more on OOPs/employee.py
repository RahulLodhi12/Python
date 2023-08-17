# salaryAfterIncrement = salary * increment 

class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , sai):
        self.increment = sai/self.salary


e = Employee()
# e.increment = 2
print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 25000 # Employee.salaryAfterIncrement(e , 25000)
print(e.increment)

