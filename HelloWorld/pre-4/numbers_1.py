import math


print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # returns exact number (decimal)
print(10 // 3)  # returns whole number
print(10 % 3)  # modulus - returns remainder
print(10 ** 3)  # exponent

print(round(2.9))  # rounds to 3
print(abs(-2.9))  # returns 2.9

# Round a number upward to its nearest integer
print(f"{'math ceiling: '} {math.ceil(2.2)}")
# Round a number downward to its nearest integer
print(f"{'math ceiling: '} {math.floor(2.2)}")


x = input("x: ")
# print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")
