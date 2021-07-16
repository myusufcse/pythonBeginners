x = input("Enter 1st Number : ")
y = input("Enter 2nd Number : ")
try:
    z = x / int(y)
except TypeError as te:
    print("asdf", te)
