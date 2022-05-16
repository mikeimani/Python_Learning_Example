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
        print("talk")

John = Person("John Smith")
print(John.name)
John.talk()