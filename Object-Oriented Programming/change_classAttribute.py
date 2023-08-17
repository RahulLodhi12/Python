class Sample:
    a = "Harry"  # class attribute


obj = Sample()

obj.a = "Rahul"  # instance attribute

print(obj.a)

Sample.a = "Vicky" # changing the class attribute

print(obj.a)