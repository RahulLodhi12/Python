class RailwayForm:
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")

harryApp = RailwayForm()
harryApp.name = "Harry"
harryApp.train = "Rajdhani Express"

harryApp.printData()