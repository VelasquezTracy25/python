numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

first, second, third = numbers


numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4]

first, second, *allothers, last = numbers

print(first)
print(second)
print(allothers)
print(last)
