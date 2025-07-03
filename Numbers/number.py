from decimal import Decimal, Context
from fractions import Fraction
import math
import random

# Decimal precision example
ctx = Context(prec=6)
result = ctx.add(Decimal('1.23456'), Decimal('7.89012'))
print("Decimal context result:", result)  # 9.12468

# Big integer power
x = 2 ** 1000
print("2 ** 1000 =", x)

# Float division
result = 1 / 3
print("1 / 3 =", result)

# str vs repr vs print
print("str('chai'):", str('chai'))       # 'chai'
print("repr('chai'):", repr('chai'))     # "'chai'"
print("print('chai'):", end=" "); print('chai')  # chai

# Boolean in conditionals
print("bool([]):", bool([]))             # False
print("bool(-1):", bool(-1))             # True
print("bool({'name': 'Alice'}):", bool({'name': 'Alice'}))  # True

# Comparison operators
print("1 < 2:", 1 < 2)                   # True
print("5.0 == 5.0:", 5.0 == 5.0)         # True
print("4.0 != 5.0:", 4.0 != 5.0)         # True

# math.floor() and math.trunc()
print("math.floor(3.5):", math.floor(3.5))       # 3
print("math.floor(-3.5):", math.floor(-3.5))     # -4
print("math.trunc(-2.8):", math.trunc(-2.8))     # -2
print("math.trunc(2.8):", math.trunc(2.8))       # 2

# Large integer precision
print("999999999999999999 + 1 =", 999999999999999999 + 1)  # Works fine

# Complex numbers
print("(2 + 1j) * 3 =", (2 + 1j) * 3)  # (6+3j)

# Number bases
print("0xFF =", 0xFF)                 # 255
print("0b1000 =", 0b1000)             # 8
print("oct(64) =", oct(64))           # '0o100'
print("hex(64) =", hex(64))           # '0x40'
print("bin(64) =", bin(64))           # '0b1000000'
print("int('64', 16) =", int('64', 16))  # 100
print("int('1000', 12) =", int('1000', 12))  # 1728

# Random module
print("random.random():", random.random())          # Random float 0–1
print("random.randint(1, 100):", random.randint(1, 100))  # Random int

li = ['lemon', 'masala', 'ginger tea']
print("random.choice(li):", random.choice(li))      # Random element
random.shuffle(li)
print("shuffled li:", li)

# Floating point precision issues
print("0.1 + 0.1 + 0.4 =", 0.1 + 0.1 + 0.4)          # May be 0.6000000000000001
print("0.1 + 0.1 + 0.1 =", 0.1 + 0.1 + 0.1)          # 0.3
print("0.1 + 0.1 + 0.1 + 0.3 =", 0.1 + 0.1 + 0.1 + 0.3)  # 0.6
print("(0.1 + 0.1 + 0.1) + 0.3 =", (0.1 + 0.1 + 0.1) + 0.3)  # 0.6

# Solving precision issue with Decimal
print("Decimal('0.1') * 3 =", Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))  # 0.3

# Fractions
myFr = Fraction(2, 7)
print("Fraction(2,7) =", myFr)  # 2/7

# Set operations
setone = {1, 2, 3, 4}
print("setone & {1,3} =", setone & {1, 3})  # Intersection
print("setone | {1,3,7} =", setone | {1, 3, 7})  # Union

# Boolean types and comparisons
print("type(True):", type(True))       # <class 'bool'>
print("True == 1:", True == 1)         # True
print("False == 0:", False == 0)       # True
print("True is 1:", True is 1)         # False (because they’re not the same object)
print("True + 4 =", True + 4)          # 5
