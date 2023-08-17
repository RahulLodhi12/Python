class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 2

    def upgradeLevel(self):
        self.level = self.level + 1


class Programmer(Freelancer , Employee):   # order of inheritance , Priority: 1st > 2nd
    name = "Rohit"


p = Programmer()
p.upgradeLevel()
print(p.company)
print(p.level)