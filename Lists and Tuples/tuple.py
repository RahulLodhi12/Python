# A tuple is an immutable (can’t change or modified) data type in Python.
t1 = (1,3,5)
print(t1)
# Once defined, tuple elements can’t be manipulated or altered.
print(t1[1])

#t1[0] = 67 # Cannot update tuple

t = () # Empty tuple
print(t)

t2 = (134) # Wrong way to declare a tuple with single element
print(t2)

t3 = (134,) # Tuple with only one element needs a comma
print(t3)