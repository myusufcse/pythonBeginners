# Three ways to use library function.
import math
print("Factorial of 5 is ", math.factorial(5))

from math import factorial
print("Factorial of 6 is ", factorial(6))

from math import factorial as fac
print("Factorial of 7 is ", fac(7))
