class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    # totalSalary = salary + salaryBonus

    @property  # The method name with @property decorator is called getter method.
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus = val - self.salary


e = Employee()
e.salaryBonus = 2000 
print(e.totalSalary)
e.totalSalary = 6666
print(e.salary)
print(e.salaryBonus)
    