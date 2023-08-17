class Employee:
    company = "Google"  # class attribute
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000  # instance attribute
harry.getSalary() # It means that:->  Employee.getSalary(harry)
# here,self is harry,and the above line of code is equivalent to Employee.getSalary(harry)
