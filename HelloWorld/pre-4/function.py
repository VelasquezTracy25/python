def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


greet("Tracy", "V")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
# file = open("content.txt", "w")
# file.write(message)


# Make code more understandable by listing parameter/argument in call

# by listing by as one, the parameter is now optional
def increment(number, secondParam, by=1):
    return number + by


print(increment(2, "none", by=2))  # returns 4
print(increment(2, "none"))  # returns 3


# *args
def multiply(*numbers):  # by adding "*" you can accept as many args as you want
    print(numbers)  # prints (2, 3, 4, 5)
    total = 1
    for number in numbers:
        total *= number
    return total


print(f"Total: {multiply(2, 3, 4, 5)}")  # Prints Total: 120

# **args - saves dictionaries by passing mulitple variables


def save_user(**user):
    print(user["id"])


save_user(id=1, name="john", age=22)
