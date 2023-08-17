# Rock paper scissors game

import random

def gameWin(comp , you):
    if comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == you:
        return None


you = input("Your's Turn: Scissor(s) , Paper(p) or Rock(r)?: ")
print(f"You chose: {you}")

# print("Computer Turn: Scissor(s) , Paper(w) or Rock(g)?")
randNo = random.randint(1,3) # from 1 to 3
# print(randNo)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='r'

print(f"Computer chose: {comp}")

# a = input("Player's Turn: Scissor(s) , Paper(p) or Rock(r)?")
# b = input("Computer Turn: Scissor(s) , Paper(p) or Rock(r)?")

# gameWin(comp , you)

if gameWin(comp,you):
    print("You Win!")
elif gameWin(comp,you)==None:
    print("Game Tie!")
else:
    print("You Lose!")
