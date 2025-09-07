class Person:
    def __init__(self, name, age):  # constructor with parameters
        self.name = name
        self.age = age

    def greet(self):  # method
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


# objects OUTSIDE the class (not indented)
p1 = Person("amine", 19)
p2 = Person("naruto", 17)

p1.greet()
p2.greet()
