# if input is divisible by 3 return "fizz"
# if input is divisible by 5 return "buzz"
# if input is divisible by 4 AND 5 return "fizzbuzz"
# if neither return the number itself


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input


# print(fizz_buzz(0))
print(fizz_buzz(1))
print(fizz_buzz(2))
print(fizz_buzz(3))
print(fizz_buzz(2))
print(fizz_buzz(5))
print(fizz_buzz(6))
print(fizz_buzz(7))
print(fizz_buzz(8))
print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(15))
