newString = "Get the length of this string. It's too long to read."
print(len(newString))
print(newString[0])
print(newString[-1])
print(newString[0:2])
print(newString[0:])
print(newString[:3])
print(newString[:])

first = "Tracy"
last = "Vel"
full = f"{first} {last}"
expression = f"{len(last)}  'seeing what this does'    {2+2}"
expression = f"{len(last)}  {'seeing what this does ' 'Yee'}    {2+2}"


print(expression)

course = "   python programming    "
print(course.upper())  # uppercase
print(course.lower())  # lowercase
print(course.title())  # Title case
print(course.strip())  # removed white space
print(course.lstrip())  # removed left white space
print(course.rstrip())  # removed right white space
print(course.find("pro"))  # returns index
print(course.replace("pro", "Repro"))  # replaces text

print("pro" in course)  # returns True
print("Pro" not in course)  # returns True
