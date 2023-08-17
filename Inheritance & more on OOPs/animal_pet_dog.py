class Animal:
    type = "Mammal"

class Pet(Animal):
    color = "White"

class Dog(Pet):
    @staticmethod
    def bark():
        print("Dog starts barking")


d = Dog()
d.bark()