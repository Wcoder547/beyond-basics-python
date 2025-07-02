#Python Object Memory Allocation
a = "Hello, World!"  # The memory is allocated for this string object

# Assigning the same object to another variable
b = a  # No new memory is allocated; 'b' references the same object as 'a'

# Printing memory addresses of 'a' and 'b'
print(f"Memory address of 'a': {id(a)}")  # Output: Memory address of 'a'
print(f"Memory address of 'b': {id(b)}")  # Output: Memory address of 'b' (same as 'a')

# Creating a new object
c = "Python"  # New memory is allocated for this different string object

# Printing memory address of 'c'
print(f"Memory address of 'c': {id(c)}")  # Output: Memory address of 'c' (different from 'a' and 'b')

#output
# Memory address of 'a': 126707795390512
# Memory address of 'b': 126707795390512
# Memory address of 'c': 11043008


# Reference Counting in Python
import sys  # Importing sys module to access reference count

# Creating an object (a list in this case)
my_list = [1, 2, 3]

# Checking the reference count of 'my_list'
print(f"Initial reference count of 'my_list': {sys.getrefcount(my_list)}")  # Output: Reference count

# Creating additional references to the same object
ref1 = my_list
ref2 = my_list

# Checking the updated reference count of 'my_list'
print(f"Updated reference count of 'my_list': {sys.getrefcount(my_list)}")  # Output: Increased reference count

# Deleting one reference
del ref1

# Checking the reference count after deletion
print(f"Reference count after deleting 'ref1': {sys.getrefcount(my_list)}")  # Output: Decreased reference count


#Python Garbage Collection
import gc  # Importing garbage collector module

# Defining a simple class to create objects
class MyClass:
    def __init__(self, name):
        self.name = name

# Creating an object instance
obj1 = MyClass("Object1")

# Checking if the object is tracked by garbage collector
print(f"Is 'obj1' tracked by GC?: {gc.is_tracked(obj1)}")  # Output: True

# Deleting the object reference
del obj1

# Forcing garbage collection
gc.collect()

# Checking the status after collection
print("Garbage collection completed.")

#Memory Leaks and Circular References

import gc

# Defining two classes to create a circular reference
class A:
    def __init__(self):
        self.b = None  # Placeholder for an instance of B

class B:
    def __init__(self):
        self.a = None  # Placeholder for an instance of A

# Creating instances of both classes
obj_a = A()
obj_b = B()

# Creating a circular reference
obj_a.b = obj_b
obj_b.a = obj_a

# Forcing garbage collection
gc.collect()

# Breaking the circular reference
obj_a.b = None
obj_b.a = None

# Forcing garbage collection again
gc.collect()

print("Circular reference has been handled.")


# Explanation:

#     Circular References: 'obj_a' references 'obj_b' and vice versa, forming a circular reference.
#     Garbage Collection Handling: Even with circular references, Python's garbage collector can detect and clean them up if references are broken ('gc.collect()').


# Optimizing Memory Usage with '__slots__'

# Without __slots__
class WithoutSlots:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# With __slots__
class WithSlots:
    __slots__ = ['name', 'age']  # Define allowed attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances
obj1 = WithoutSlots("Alice", 30)
obj2 = WithSlots("Bob", 25)

# Checking the memory sizes
import sys
print(f"Memory usage without __slots__: {sys.getsizeof(obj1)} bytes")  # Output: Memory size
print(f"Memory usage with __slots__: {sys.getsizeof(obj2)} bytes")  # Output: Reduced memory size


# Explanation:

#     '__slots__' Usage: Reduces memory usage by preventing the creation of a default '__dict__' for each instance.
#     Memory Optimization: The memory footprint is smaller for 'WithSlots' than for 'WithoutSlots'.

# Using Weak References

import weakref  # Importing weakref module

# Defining a class to create objects
class MyClass:
    def __init__(self, name):
        self.name = name

# Creating a strong reference
obj = MyClass("MyObject")

# Creating a weak reference to the object
weak_obj = weakref.ref(obj)

# Checking if weak reference is alive
print(f"Is weak reference alive?: {weak_obj() is not None}")  # Output: True

# Deleting the strong reference
del obj

# Checking if weak reference is still alive
print(f"Is weak reference alive after deleting strong reference?: {weak_obj() is not None}")  # Output: False


# Monitoring Memory Usage with psutil

# psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes.

import psutil  # Importing the psutil module to monitor system performance

# Function to check memory usage
def memory_usage():
    process = psutil.Process()  # Get the current process
    mem_info = process.memory_info()  # Get memory information
    print(f"Memory usage: {mem_info.rss / (1024 * 1024):.2f} MB")  # Print memory usage in MB

# Creating a large list
large_list = [i for i in range(1000000)]

# Checking memory usage
memory_usage()  # Output: Memory usage before clearing the list

# Clearing the list to free memory
large_list.clear()

# Checking memory usage after clearing the list
memory_usage()  # Output: Reduced memory usage after clearing


# Explanation:

#     'psutil' Library: Provides utilities to monitor memory and system performance.
#     Memory Monitoring: Demonstrates how memory usage changes before and after freeing up resources.
