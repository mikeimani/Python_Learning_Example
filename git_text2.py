# If statements
temperature = 35

if temperature > 30:
    print("It is a hot day")
    print("Drink plenty of water")

# elif statements

temperature = 25

if temperature > 30:
    print("It is a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It is a nice day")
print("Done")

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))


is_hot = False
is_cold = True

if is_hot:
    print("It is a hot day")
    print("Drink plenty of  water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It is a lovely day")

# File 2




