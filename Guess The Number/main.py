import random
randNumber = random.randint(1,100)
# print(randNumber)

userGuess = None
guessNo = 0

while(userGuess!=randNumber):
    userGuess = int(input("Enter your guess: "))
    guessNo+=1
    if(userGuess==randNumber):
        print("You guessed it Right!")
    
    else:
        print("You guessed it Wrong!")
        if(userGuess>randNumber):
            print("*********Enter a smaller no.*********")
        else:
            print("*********Enter a larger no.*********")


print(f"Your guessed it in {guessNo} guesses.")

with open("bestScore.txt","r") as f:
    bestScore = int(f.read())

if(guessNo<bestScore):
    print("You just broke the best score")
    with open("bestScore.txt","w") as f:
        f.write(str(guessNo))