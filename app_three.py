
# if statements
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

# exercise 3
weight = int(input("Weight: "))
decision = str(input("(K)g or (L)bs: "))

if decision.upper() == "L":
    print("Weight in Kgs: ", round(weight * 0.45))
if decision.upper() == "K":
    print("Weight in Lbs: ", round(weight / 0.45))

# while loops
i = 1
while i <= 5:
    print(i * "*")
    i = i + 1

# lists
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3])
print(names)

# list methods
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)
numbers.clear()
print(1 in numbers)
print(numbers)
