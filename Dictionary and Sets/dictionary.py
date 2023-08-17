d = {
    "Key":"value",
    "Harry":"code",
    "list":[1,2,3],
    "marks":100,
    "d1" : {"rahul":"smart"}
}

# Dictionary is a collection of key-value pairs.

print(d["Key"]) # It is indexed and access by using keys.
print(d["Harry"])
print(d["list"])
d["marks"] = 55  # It is mutable and It cannot contain duplicate keys.
# Ek name ki ek key should be in a single dictionary.
print(d["marks"])

print(d["d1"]["rahul"])

print(d) # Dictionary is unordered.