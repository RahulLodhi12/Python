def replace_split(string, word):
    newString = string.replace(word,"")
    return newString.strip()


text = "    BCCI IPL ICC     "
print(text)
print(text.strip())
print(replace_split(text," IPL"))