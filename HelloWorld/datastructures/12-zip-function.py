list1 = [1, 2, 3]
list2 = [10, 20, 30]

# goal: [(1,10), (2,20), (3,30)]

print(list(zip("abcdefg", list1, list2)))
