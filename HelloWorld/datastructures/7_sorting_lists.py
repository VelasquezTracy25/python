numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers))
print(sorted(numbers, reverse=True))


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# function that can help sort list - will return a list like 10, 9,12 - so python sorts the list by the numbers (by price)


def sort_item(item):
    print(f"{item[1]}")
    return item[1]


items.sort(key=sort_item)  # need
print(items)
