# Python has an open() function(built-in) for opening files.
# It takes 2 parameters: filename and mode.
# Here, “sample” is the file name and “r” is the mode of opening (read mode)

# f = open("sample.txt","r")
f = open("sample.txt") # By default mode is r
data = f.read() # Called only one time
# data = f.read(4) # read first 4 characters
print(data)
f.close()