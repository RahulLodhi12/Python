num1 = int(input("Enter no. 1: "))
num2 = int(input("Enter no. 2: "))
num3 = int(input("Enter no. 3: "))
num4 = int(input("Enter no. 4: "))

if (num1>num4):
    f1 = num1
else:
    f1 = num4

if (num2>num3):
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print(f1, "is the greatest")
else:
    print(f2, "is the greatest")
