# While loops
guess_count = 1
while guess_count <= 5:
    print(guess_count)
    guess_count = guess_count + 1
# Lists use []
names = ["Key", "John"," Bob", "Joe"]
print(names)

# For loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# Range function
numbers = range(5, 12, 3)
for number in numbers:
    print(number)
    
# Tuples use ()
numbers = (1, 2, 3, 4)

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")

prices = [10, 20, 40]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested loops

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)




# File 1 , 2, 3