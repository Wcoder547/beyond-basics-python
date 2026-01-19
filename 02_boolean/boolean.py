# boolean - true or false values

# ================================Truthy Values================================
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

print(bool("Hello"))  # True
print(bool(15))       # True
print(bool(["apple", "cherry", "banana"]))  # True

# ================================Falsy Values=================================
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False    


#===============================isinstance() Function==========================
x=200
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False