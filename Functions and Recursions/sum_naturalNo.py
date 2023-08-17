# sum(n) = n + sum(n-1)
def natural(n):
    if n==1:
        return 1
    else:
        return n + natural(n-1)
    

print(natural(4))
