#Question No 1.
import time 

# Decorator to calculate execution time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the actual function
        end = time.time()  # Record end time
        print(f"{func.__name__} ran in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)  # Simulate a long task

example_function(2)  # OUTPUT: example_function ran in 2.00XX seconds


#Question No 2.
# Decorator to debug function call
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args ({args_value}) and kwargs {{{kwargs_value}}}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("chai", greeting="hanji")
# OUTPUT:
# Calling: greet with args (chai) and kwargs {greeting=hanji}
# hanji, chai!



#Question No 3.
import time

# Decorator to cache function results
def cache(func):
    cache_value = {}  # Dictionary to store previous results
    def wrapper(*args):
        if args in cache_value:
            print(f"Fetching from cache for {args}")
            return cache_value[args]
        print(f"Computing result for {args}")
        result = func(*args)
        cache_value[args] = result  # Save result to cache
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate expensive computation
    return a + b

print(long_running_function(2, 3))  # Takes 4 seconds first time
print(long_running_function(2, 3))  # Instant the second time
