items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# Basic Way
prices = []

for item in items:
    prices.append(item[1])

print(prices)

# Map Way

newprices = list(map(lambda item: item[1], items))

print(newprices)
