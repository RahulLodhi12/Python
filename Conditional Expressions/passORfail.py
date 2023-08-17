s1 = int(input("Enter per%age of s1: "))
s2 = int(input("Enter per%age of s2: "))
s3 = int(input("Enter per%age of s3: "))

total = s1 + s2 + s3 

if(s1<33 or s2<33 or s3<33):
    print("You are Fail")
elif(total/3)<40:
    print("You are Fail <40")
else:
    print("You Passed the exam")