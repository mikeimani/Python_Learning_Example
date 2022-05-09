# Format

first = "John"
last = "Smith"
message = f'{first} [{last}] is a coder'
print(message)

# String Methods

course ='Python for Beginners'
print(len(course))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Newbies'))

price = 1000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'down_payment: ${down_payment}')

weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} Kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
