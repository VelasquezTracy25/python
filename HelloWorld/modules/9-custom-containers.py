class TagCloud:
    # Contructors - initialize as a tag dictionary
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        # supply default value of 0 if key doesnt have count, if not increment by 1
        # Count at key = get key and check
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    # Gets value at given tag, other wise return 0
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # Sets value to given count (manual)
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    # Gets number of items in the dictionary TagCloud
    def __len__(self):
        return len(self.__tags)

    # returns an iterater object that returns one item at a time in a for loop
    def __iter__(self):
        return iter(self.__tags)


cloud1 = TagCloud()
cloud1.add("Python")
cloud1.add("python")
cloud1.add("python")
cloud1.add("java")
cloud1.add("python")
cloud1.add("python")

# print(cloud1.__tags) ##This would no longer work because its private
print(cloud1.__dict__)  # prints {'_TagCloud__tags': {'python': 5, 'java': 1}}
print(cloud1._TagCloud__tags)
