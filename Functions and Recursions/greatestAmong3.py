# Universal Method for greatest among 3 nos.
def maximum(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3

num = maximum(300,30,300)
print("The maximum value among three no.: " + str(num))