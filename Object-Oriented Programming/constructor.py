class Employee:
    company = "Google"  # class attribute

#     __init__() is a special method which runs as soon as the object is created.
#     __init__() method is also known as constructor.
#     It takes self-argument and can also take further arguments.

    def __init__(self , name , salary , subunit):
        self.name = name   #  self refers to the object
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getDetail(self):
        print(f"Name of employee is {self.name}")
        print(f"Salary of employee is {self.salary}")
        print(f"Subunit of employee is {self.subunit}")

# harry = Employee() # Employee.__init__(harry)
harry = Employee("harry", 10000 , "Youtube")
# harry = Employee() -> This throws an error (missing 3 positional arguments)
harry.getDetail()