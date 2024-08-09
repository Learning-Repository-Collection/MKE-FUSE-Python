# keyword argument
def increment(number, by):
    return number + by


print(increment(2, by=1))


# default arguments
def increment_one(number, by=1):
    return number + by


print(increment_one(2))
print(increment_one(2, 5))


# number of arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# **args
def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="John", age=22)

# scope
message = "a"


def greet(name):
    # global message (avoid this)
    message = "b"


greet("Mosh")
print(message)


# last exercise
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
