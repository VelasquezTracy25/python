# Conditional statements

temperature = 25

if temperature > 30:
    print("It's warm")
    print("Drink Water")
elif temperature > 20:
    print("Chilly")
else:
    print("It's perfect")
print("Done")


# Ternary

age = 22

if age >= 18:
    message = "Eligible"
else:
    message = "Not elible"

print(message)

message = "Eligible" if age >= 18 else "Not Eligible"

print(message)


# Logical Operators

high_income = True
good_credit = True

# and

print("Eigible because both are True") if high_income and good_credit else print(
    "Not Eligible")

# or

print("Eigible because at least one is True") if high_income or good_credit else print(
    "Not Eligible")

# Short-circuit Evaluation
# If the first section of the evaluation does not match then the evaluation just stops


# Chaining comparison operators

age = 22
if 18 <= age < 65:
    print("Eligible because of Chaining")


# For Loops

# range (start, end, step)

for number in range(3, 10, 3):
    print("Count", number+1, (number + 1) * ".")


# For Loop with Conditionals

successful = False

for number in range(10):
    print("Attempt")
    if successful:
        print("Successful")
        break
    else:
        print("Attempted 10 times and not Successful")

# Nested for loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterables

print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)

# While Loop
# prints 100, 50, 25, 12, 6, 3, 1
number = 100

while number > 0:
    print(number)
    number //= 2  # halfs number variable


# command = ""
# while command != "Quit":
#    command = input("Enter an algorithm")
#    print("ECHO", command)


# Avoid infinite loop by breaking if the word quit is input
# while True:
#     command = input("Enter Input: ")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


# Quiz: Print  2, 4, 6, 8 and then We have 4 even numbers
count = 0

for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1

print(f"We have {count} even numbers")
