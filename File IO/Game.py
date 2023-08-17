def game():
    return 5214

with open("Hiscore.txt") as f:
    Hiscore = f.read()

Score = game()

if  Hiscore=='' or int(Hiscore)<Score:
    with open("Hiscore.txt","w") as f:
        f.write(str(Score))