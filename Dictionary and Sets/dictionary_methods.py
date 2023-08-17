d = {
    "key":"value",
    "harry":"code",
    "list":[1,2,3],
    "marks":100,
    "d1" : {"rahul":"smart"},
    264 : 400
}

print(type(d.keys())) # <class 'dict_keys'>
print(d.keys()) # returns dictionary’s keys.
print(list(d.keys())) # convert dict_keys to list.

print(d.values()) # returns dictionary's values

print(d.items()) # returns (key,value) tuple.

# updateDic = {
#     "friend" : "sam"
# }
d.update({"friend" : "sam"}) # updates the dictionary with supplied key-value pairs.
print(d)

print(d.get("harry")) # Print value associated with key "harry"
print(d["harry"]) # Print value associated with key "harry"

# The difference b/w .get and [] syntax in dictionaries
print(d.get("harry2")) # returns None as harry2 is not present in dictionary
print(d["harry2"]) # throws error as harry2 is not present in dictionary


