class Remote:
    pass

class Player:
    def moveLeft(self):
        pass
    
    def moveRight(self):
        pass

    def Jump(self):
        pass


remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed):
    player1.moveLeft()

# objectName.Attributes

'''
Modelling a problem in OOPs :-
We identify the following in our problem
Noun -> Class -> Employee
Adjective -> Attributes -> name,age,salary
Verbs -> Methods -> getSalary(), increment()
'''

'''
OOPs consists 3 items :-> Class , Attributes , Methods
Eg:
Class -> Employee
Attributes -> name,age,salary
Methods -> getSalary() , increment()
'''