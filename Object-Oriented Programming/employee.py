class Employee:
    company = "Google"  # company is the attribute or class attribute
    # salary = 100   # class attribute

harry = Employee()   #Object instantiation, harry is a object of Employee class
rahul = Employee()   #Object instantiation, rahul is a object of Employee class

harry.salary = 300   # instance attribute
rahul.salary = 400   # instance attribute

print(harry.company)
print(rahul.company)

Employee.company = "Youtube"   #changing class attribute

print(harry.company)
print(rahul.company)

print(harry.salary)
print(rahul.salary)