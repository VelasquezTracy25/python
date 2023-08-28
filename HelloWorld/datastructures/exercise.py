sentence = "This is a common interview question"

# Find the most repeate character in the sentence - common interview question

# Questions to ask: Are capitalized chars and spaces counted? Should they be lower case.

# go through each one and maybe get a count of the letters, then see which count is the highest
# Guess is maybe use a dictionary and have them sorted by greatest to least

char_freq = {}

for char in sentence:  # loop through and make a dictionary of counts

    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

char_freq_sorted = sorted(  # sort all key values pairs as tuples, biggest first

    char_freq.items(),
    key=lambda kv: kv[1],
    reverse=True)

# return the first item of the sorts list (the char 'i')
print(char_freq_sorted[0])
