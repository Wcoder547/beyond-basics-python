# Question No 1.
def square_of_num(number):
    return number ** 2

result = square_of_num(4)
print(result)

# Question No 2.
def add(numOne, numTwo):
    return numOne + numTwo

print(add(5, 5))

# Question No 3.
def multiply(p1, p2):
    return p1 * p2

print(multiply(8, 5))
print(multiply('a', 5))
print(multiply(5, "h"))

# Question No 4.
import math
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumFerence = 2 * math.pi * radius
    return area, circumFerence

a, c = circle_stats(3)
print("Area:", a, "CircumFerence:", c)

# Question No 5.
def greet(name):
    return "Hello, " + name + " !"

print(greet("Waseem"))

# Question No 6.
cube = lambda x: x ** 3
print(cube(3))

# Question No 7.
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

# Question No 8.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="waseem akram", power="lazer", enemy="Dr.jackaal")

# Question No 9.
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)

# Question No 10.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

 