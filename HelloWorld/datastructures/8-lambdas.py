# lambdas - one line anonymous function that can be passed to other functions


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# function that can help sort list - will return a list like 10, 9,12 - so python sorts the list by the numbers (by price)

# def sort_item(item):
#     print(f"{item[1]}")
#     return item[1]

# this top function can be reduce to the lambda below because it will only ever be used in this instance for sorting
items.sort(key=lambda item: item[1])
print(items)
