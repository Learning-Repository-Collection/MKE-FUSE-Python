# functions
def greet_one():
    print("Hi There")
    print("Welcome Aboard")


greet_one()


# arguments
def greet_two(first_name, second_name):
    print(f"Hi {first_name} {second_name}")
    print("Welcome aboard")


greet_two("Mosh", "Hamedani")
greet_two("John", "Smith")


# types of functions
def greet_three(name):
    print(f"Hi {name}")


def greet_four(name):
    print(f"Hi {name}")


def greet_five(name):
    return f"Hi {name}"


message = greet_five("Mosh")
file = open("content.txt", "w")
file.write(message)

print(greet_four("Mosh"))
