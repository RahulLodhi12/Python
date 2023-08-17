# Creating a empty set
b = set()
print(type(b))

# Adding elements to an empty set
b.add(2)
b.add(5)
b.add(5) # Adding a element repeatedly does not changes a set 

#b.add([7,8]) # Cannot add list to an set, because list can be updated and sets follows no updation rule.

b.add((5,6)) # Can add tuple to an set, because tuple and sets follows no updation rule.

#b.add({4:7}) # Cannot add dictionary to an set, because dictionary can be updated and sets follows no updation rule.

print(b)

print(len(b)) # Returns the length of the set.

b.remove(5) # removes 5 from b.
print(b)

print(b.pop())
print(b) # Removes an arbitrary element(koi bhi element) from the set and returns the element removed.

b = b.union({1,3,7})
print(b)

b = b.intersection({3,11})
print(b)