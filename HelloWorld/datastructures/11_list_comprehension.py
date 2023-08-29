items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# Prints filtered list of items greater than or equal to 10: [('product1', 10), ('product3', 12)]
prices = list(map(lambda item: item[1], items))
prices1 = [item[1] for item in items]  # cleaner way to map and filter lists

print(prices1)


# Prints filtered list of items greater than or equal to 10: [('product1', 10), ('product3', 12)]
filtered = list(filter(lambda item: item[1] >= 10, items))
# cleaner way to map and filter lists
filtered1 = [item for item in items if item[1] >= 10]
print(filtered1)
