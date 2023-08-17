dict = {
    "Namaste" : "Hello",
    "Vastu" : "Item",
    "Pankha" : "Fan",
    "Dabba" : "Box" 
}

print("Options are: ",dict.keys())
a = input("Enter Hindi Word: ")
# print("English Meaning: ",dict[a])

# Below line will not throw an error even the key is not present in the dictionary.
print("English Meaning: ",dict.get(a))