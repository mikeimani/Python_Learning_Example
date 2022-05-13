# Functions

def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")



def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")


print("Start")
greet_user('John')
print("Finish")

def square(number):
    return number * number

print(square(3))

# Exceptions

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalide value")
