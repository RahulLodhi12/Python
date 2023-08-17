class Number:
    def __init__(self,num):
        self.num = num
        # print("Hello")

    def __add__(self , num2):
        print("Lets add")
        return self.num + num2.num

    def __mul__(self , num2):
        print("Lets multiple")
        return self.num * num2.num


n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

'''
p1 + p2 -> p1.__add__(p2)

p1 - p2 -> p1.__sub__(p2)

p1 * p2 -> p1.__mul__(p2)

p1 / p2 -> p1.__truediv__(p2)

p1 // p2 -> p1.__floordiv__(p2)
'''