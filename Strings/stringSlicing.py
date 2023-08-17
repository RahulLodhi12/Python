name = "Harry"
# print(name[4])
# name[3] = 'd' --> TypeError: 'str' object does not support item assignment / Doesn't work

print(name[0:3]) # Elements from 0(start) to 3-1(end-1)
# name[start:end]
print(name[1:4]) # Elements from 1(start) to 4-1(end-1)

print(name[:3]) # Elements from 0(start) to 3-1(end-1)
print(name[0:]) # Elements from 0(start) to end

# Negative Indices: Negative indices can also be used as shown in the name[start,end]. -1 corresponds to the (length-1) index, -2 to (length-2).

c = name[-4:-1] # it is same as name[1:4]
print(c)

# Slicing with skip value
# We can provide a skip value as a part of our slice like this:
word = "amazing"
print(word[1:6:2]) # Skipped every 2nd element