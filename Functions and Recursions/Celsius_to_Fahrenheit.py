def tempConvert(c):
    f = ((c * 9/5) + 32)
    return f 

t = int(input("Enter an temp. value: "))
temp = tempConvert(t)
print(f"The temp. of {t} celsius in fahrenheit: " + str(temp) )