print("Scalar data types: \n\tintegers, \n\tfloats, \n\tNone (str) and \n\tbool")

# Assigning multiple values to multiple variables
a, b, c = 5, 3.2, "Hello"

print(a)
print(b)
print(c)

# assign the same value to multiple variables at once
x = y = z = "same"

print(x)
print(y)
print(z)

# To write multiple statements in the line use ;
z = "not same"; print(y); print(z)

# int type
a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# float type
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

# Constant should be full uppercase But we can change the value here.
PI = 13.14
PI = PI - 10

# str type
strings = "This is Python"
char = "C"
string1 = None  # similar to null in java which is nothing

# use , to concatenate the strings. similar + in java
print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)
print(PI)
print(strings, char, string1)

# bool type True or False
x = (1 == True)
y = (1 == False)
a = True + 4  # True is 1
b = False + 10  # False is 0

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
print("all the below stmt return False")
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(""))  # False ? empty string
print(bool({}))  # False ? empty dict
print(bool([]))  # False ? empty list
print(bool(()))  # False ? empty tuple

print("all the below stmt return True")
# Rest is True
print(bool("True"))  # True
print(bool("False"))  # True
print(bool("0"))  # True
print(bool(0.01))  # True
print(bool(-12))  # True
print(bool(2))  # True

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits, " is a ", type(fruits))
print(numbers, " is a ", type(numbers))
print(alphabets, " is a ", type(alphabets))
print(vowels, " is a ", type(vowels))

# type is used to find the type of variable or class name.
print(type(1))
print(type(1.2))
print(type("me"))
print(type(False))
