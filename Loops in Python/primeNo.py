n = int(input("Enter a no.: "))

flag = False
for i in range(2,n):
    if n%i==0:
        print("Not Prime")
        break
    else:
        flag = True

if(flag):
    print("Prime No.")