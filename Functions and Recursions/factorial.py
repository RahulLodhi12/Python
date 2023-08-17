# n! = 1*2*3*...*n
# n = 0
# fact=1
# for i in range(1,n+1):
#     fact = fact*i 

# print(fact)

# Using Recursion
# n! = 1*2*3*...*n
# n! = [1*2*3*...(n-1)]*n
# n! = n * (n-1)!
def factorial(n):
    if n==0 or n==1: # base condn
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))

# The programmer needs to be extremely careful while working with recursion 
# to ensure that the function doesn’t infinitely keep calling itself.

# Recursion is sometimes the most direct way to code an algorithm.