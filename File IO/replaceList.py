words = ["donkey" , "kaddu", "mote"]

with open("sample.txt","r") as f:
    data = f.read()

for word in words:
    data = data.replace(word,"#$#$#$")

with open("sample.txt","w") as f:
    f.write(data)