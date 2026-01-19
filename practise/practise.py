import random

print(random.randrange(1,10))
print("Hello world",end=" ")
print("i will write on same line")

print("i am",35,"years old ")

x=5
y=6
print("value of x is",x,"and value of y is", y)
x="override"
print(x)
x=str(x)
print(type(x))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

a="Hell0"
b="How are you"
print(a+b)


d="awesome"

def hello():
    d = "fantastic"
    print(d)
hello() 
print("Python is " + d) 



v = range(6)
print(v)

g = b"Hello"
print(g)
h=bytearray(5)
print(h)
print(type(h))

x = memoryview(bytes(5))
print(x)

x = None
print(x)

print("bool([]):", bool([]))  

    #  print("5 is greater then 2")