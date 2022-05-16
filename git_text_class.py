class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()

# Constructors

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
print(point1.x)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}")

John = Person("John Smith")
John.talk()

# Inheritance

class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    pass
class Cat(Mammal):
    pass
dog1 = Dog()
dog1.walk()
