class Employee:
    company = "Google"  # company is the attribute or class attribute
    salary = 100   # class attribute

harry = Employee()   #Object instantiation , harry is a object of Employee class
rahul = Employee()   #Object instantiation, rahul is a object of Employee class

# harry.salary = 300   # instance attribute
# rahul.salary = 400   # instance attribute

harry.salary = 33

print(harry.salary)
print(rahul.salary)

# Below line throws an error as address is not present in instance/class attribute
# print(rahul.address)