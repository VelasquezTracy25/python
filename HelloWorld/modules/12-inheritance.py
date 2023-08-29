# eat appears in both Mammal and Fish, if there was a bug in the duplicate code, you'd have to fix it everywhere the method was repeated

class Mammal:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")

# New Way
# Parent Class


class Animal:
    # This will be inheritted by Mammal and Fish anf set default age as 1
    def __init__(self):
        self.age = 1

    # This will be inheritted by Mammal and Fish and set default eat eaction as "eat"
    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)

f = Fish()
f.eat()
print(m.age)
