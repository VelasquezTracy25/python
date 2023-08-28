# before:

# try:
#     file = open("app.py")
#     age = int(input("Age: "))
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No Exceptions were thrown")
# finally:
#     file.close()

# Does the same but With does not need finally clause
try:
    with open("app.py") as file:
        print("File Opened")
    age = int(input("Age: "))
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No Exceptions were thrown")
