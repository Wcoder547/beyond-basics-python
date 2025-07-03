# ✅ Major difference between list and tuple: mutability
# - Lists are mutable (can be modified)
# - Tuples are immutable (cannot be modified)

tea_types = ("Black tea", "Green", "Oolong")
print("Original tuple:", tea_types)
print("First tea type:", tea_types[0])

# ❌ This line will cause a TypeError because tuples are immutable
# tea_types[0] = "change"  # Uncommenting this will raise: TypeError

# You can still find length
print("Length of tuple:", len(tea_types))

# Tuples can be concatenated to make new tuples
more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print("Concatenated tuple:", all_tea)

# Tuple type check
print("Type of tea_types:", type(tea_types))  # <class 'tuple'>

# ✅ Additional add-ons:
# ✅ Tuples can contain mixed data types
mixed_tuple = ("Masala", 2, True)
print("Mixed data tuple:", mixed_tuple)

# ✅ You can nest tuples
nested_tuple = (("green", "black"), ("hot", "cold"))
print("Nested tuple:", nested_tuple)

# ✅ You can iterate over a tuple just like a list
for tea in tea_types:
    print("Tea variety:", tea)

# ✅ You can convert tuple -> list to modify it
tea_list = list(tea_types)
tea_list[0] = "Changed tea"
print("Modified list version of tuple:", tea_list)

# ✅ Then convert back to tuple if needed
tea_types = tuple(tea_list)
print("Reconverted to tuple:", tea_types)
