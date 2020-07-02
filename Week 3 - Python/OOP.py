# OOP

# Inheritance
# Polymorphism
# Encapsulation
# Abstraction


class Dog:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        return "woof woof"
fido = Dog("canine", "black")
print(fido.color)