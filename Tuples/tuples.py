# Tuples are used to store multiple items in a single variable
# Tuple items are ordered, unchangeable, and allow duplicate values.


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


tea_types = ("Black tea", "Green", "Oolong")
print("Original tuple:", tea_types) # ('Black tea', 'Green', 'Oolong')
print("First tea type:", tea_types[0]) # Black tea

print("Length of tuple:", len(tea_types)) # 3

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print("Concatenated tuple:", all_tea) # ('Herbal', 'Earl Grey', 'Black tea', 'Green', 'Oolong')


print("Type of tea_types:", type(tea_types))  # <class 'tuple'>


mixed_tuple = ("Masala", 2, True)
print("Mixed data tuple:", mixed_tuple) # ('Masala', 2, True)


nested_tuple = (("green", "black"), ("hot", "cold"))
print("Nested tuple:", nested_tuple) # (('green', 'black'), ('hot', 'cold'))

for tea in tea_types:
    print("Tea variety:", tea) 


tea_list = list(tea_types)
tea_list[0] = "Changed tea"
print("Modified list version of tuple:", tea_list) # ['Changed tea', 'Green', 'Oolong']


tea_types = tuple(tea_list)
print("Reconverted to tuple:", tea_types) # ('Changed tea', 'Green', 'Oolong')


thistuple= tuple(("Apple", "Banana", "Cherry"))
print("Tuple created with tuple() constructor:", thistuple) # ('Apple', 'Banana', 'Cherry')


for i in range(len(thistuple)):
    print("Element at index", i, ":", thistuple[i])

print(len(thistuple)) # 3
print(range(len(thistuple))) # range(0, 3)


(a,b,c)=thistuple
print(a,b,c) # Apple Banana Cherry


# ================================= Tuple Methods =================================

# Method 	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
