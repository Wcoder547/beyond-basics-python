# ✅ Example 1: Global Variable Usage
a = 5

def function(): 
    global a  # Use the global 'a' instead of creating a local one
    print("Before changing, a =", a)  # Should print 5
    a = 10  # Update global variable 'a'
    print("After changing, a =", a)   # Should print 10

function()
print("Global a after function call:", a)  # Confirm global 'a' is now 10


# ✅ Example 2: Closure Example – Function Inside a Function
def f1():
    x = 88  # This is in the enclosing scope of f2
    def f2():
        print("Value from closure:", x)  # f2 uses x from f1
    return f2  # Return the inner function

myResult = f1()  # myResult now holds reference to f2, with access to x=88
myResult()       # Should print: Value from closure: 88


# ✅ Example 3: Function Factory using Closure
def chaicoder(num):  # Outer function with parameter `num`
    def actual(x):   # Inner function that uses `num` from outer scope
        return x ** num
    return actual  # Return the inner function

f = chaicoder(2)  # f becomes a function that squares numbers
g = chaicoder(3)  # g becomes a function that cubes numbers

print("Function f (square):", f)  # Prints function reference
print("Function g (cube):", g)    # Prints function reference

print("f(3) =", f(3))  # 3^2 = 9
print("g(3) =", g(3))  # 3^3 = 27



# Closure to keep track of count
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

#Add-On 2: Lambda with Closure
def power_maker(n):
    return lambda x: x ** n  # Returns an anonymous function that remembers n

square = power_maker(2)
cube = power_maker(3)

print("square(4) =", square(4))  # 16
print("cube(2) =", cube(2))      # 8


#Add-On 3: Function Scope vs Global vs Nonlocal

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



#Add-On 4: Common Mistake in Closures in Loops (Late Binding)
functions = []

for i in range(3):
    def make_func(n):
        def f():
            print(n)
        return f
    functions.append(make_func(i))

for fn in functions:
    fn()  # Correct: prints 0, 1, 2
