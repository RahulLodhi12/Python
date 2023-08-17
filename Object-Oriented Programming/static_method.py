import datetime
class Employee:
    company = "Google"  # class attribute
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}.\n{signature}")
    
    # Sometimes we need a function that doesn’t use the self-parameter. 
    # We can define a static method like this:
    @staticmethod  #decorator
    def greet():
        print("Good Morning, Sir!")

    @staticmethod
    def time():
        print(datetime.datetime.now())

harry = Employee()
harry.salary = 100000  # instance attribute
harry.getSalary("Thanks!") # It means that:->  Employee.getSalary(harry)
# here,self is harry,and the above line of code is equivalent to Employee.getSalary(harry)

harry.greet() # Employee.greet()

harry.time()
