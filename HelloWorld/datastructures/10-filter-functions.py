items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

x = list(filter(lambda item: item[1] >= 10, items))
# Prints filtered list of items greater than or equal to 10: [('product1', 10), ('product3', 12)]
print(x)
