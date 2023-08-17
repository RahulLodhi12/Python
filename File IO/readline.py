# Other methods to read the file :-
# We can also use f.readline() function to read one full line at a time.
f = open("sample.txt")
# Read first line
data = f.readline()
print(data)

# Read second line
data = f.readline()
print(data)

# Read third line...and so on.
data = f.readline()
print(data)

f.close()