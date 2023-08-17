class Employee:        #Base Class or Parent Class
    company = "Google"
    def showDetails(self):
        print("This is a employee")

class Programmer(Employee):      #Derived class or child class
    language = "Python"
    company = "Youtube"
    def getInfo(self):
        print(f"Employee is using {self.language}")

    def showDetails(self):
        print("This is a programmer")


e = Employee()
e.showDetails()

p = Programmer()
p.showDetails()
print(p.company)


'''
Type of Inheritance:-
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
'''
