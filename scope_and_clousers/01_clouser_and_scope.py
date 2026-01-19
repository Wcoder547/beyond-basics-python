a = 5

def function(): 
    global a  
    print("Before changing, a =", a)  
    a = 10  
    print("After changing, a =", a)  

function()
print("Global a after function call:", a)  



def f1():
    x = 88  
    def f2():
        print("Value from closure:", x)  
    return f2 

myResult = f1() 
myResult()       


def chaicoder(num): 
    def actual(x):  
        return x ** num
    return actual 

f = chaicoder(2) 
g = chaicoder(3) 

print("Function f (square):", f)  
print("Function g (cube):", g)    

print("f(3) =", f(3))  # 3^2 = 9
print("g(3) =", g(3))  # 3^3 = 27




def counter():
    count = 0
    def increment():
        nonlocal count  # Use 'nonlocal' to modify the outer function variable
        count += 1
        return count
    return increment

count1 = counter()
print(count1())  # 1
print(count1())  # 2

count2 = counter()
print(count2())  # 1 (separate instance)
print(count1())  # 3 (continues from previous count1)


def power_maker(n):
    return lambda x: x ** n  

square = power_maker(2)
cube = power_maker(3)

print("square(4) =", square(4))  # 16
print("cube(2) =", cube(2))      # 8




x = "global"

def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
        print("Inner:", x)
    inner()
    print("Outer after inner:", x)

outer()
print("Global:", x)




functions = []

for i in range(3):
    def make_func(n):
        def f():
            print(n)
        return f
    functions.append(make_func(i))

for fn in functions:
    fn()  # Correct: prints 0, 1, 2
