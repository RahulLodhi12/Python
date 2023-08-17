# The best way to open and close the file automatically is the “with” statement.
# There is no need to write f.close() as it is done automatically.
with open("another.txt","r") as f:
    data = f.read()

print(data)

with open("another.txt","a") as f:
    f.write(" Hello guy I am Rahul.")
