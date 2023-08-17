n = int(input("Enter a no.: "))

for i in range(1,n+1):
    print(" " * (n-i), end=" ") # end=" " ->  print without newline.
    print("*" * (2*i-1), end=" ")
    print(" " * (n-i))