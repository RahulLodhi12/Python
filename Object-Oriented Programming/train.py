class Train:
    def __init__(self,name,fare,seats): # used for initialization
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("***************")
        print(f"The name of train is {self.name}")
        print(f"The seats available in train are {self.seats}")
        print("***************")

    def getFareInfo(self):
        print(f"The fare of train is Rs.{self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket is booked! and your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry, train is full!")

    def cancelTicket(self , seatNo):
        pass

Intercity = Train("Intercity express: 192013" , 120 , 400)

Intercity.getStatus()
# Intercity.getFareInfo()
Intercity.bookTicket()
Intercity.getStatus()