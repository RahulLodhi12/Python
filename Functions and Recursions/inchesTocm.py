def length(i):
    cm = i*(2.54)
    return cm

len = int(input("Enter an length value: "))
l = length(len)
print(f"The length of {len} inches in cm: " + str(l) )