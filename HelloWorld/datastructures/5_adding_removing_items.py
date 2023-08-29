letters = ["a", "b", "c"]

# add items

letters.append("d")
letters.insert(0, "-")  # to prepend  ("prepend" is not a thing)
# letters.prepend("aa")

print(letters)

# remove

letters.pop()  # removes last
letters.pop(0)  # remove by index
letters.remove("b")  # finds first occurence of b and removes

# if you want to remove all "b"s you would have to loop through letters and remove one by one

print(letters)


letters2 = ["a", "b", "c", "d", "e", "f", "g"]

print(letters2)


del letters2[0:3]  # allows you to remove a whole range

print(letters2)

letters2.clear()  # clears out list

print(letters2)
