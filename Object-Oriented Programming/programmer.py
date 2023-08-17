class Programmer:
    company = "Microsoft"
    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Name of the {self.company} employee is {self.name}")
        print(f"Product is {self.product}")

harry = Programmer("Harry" , "Skype")
rahul = Programmer("Rahul" , "Github")
harry.getInfo()
rahul.getInfo()