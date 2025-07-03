tea_varities = ["black tea", "Green tea", "Oolong", "white"]
print(tea_varities)

print(tea_varities[0])          # First item
print(tea_varities[1:3])        # Slice: index 1 and 2

# Replace index 1 (Green tea) with each character of "Lemon" (bad idea)
tea_varities[1:2] = "Lemon"
print("Replacing with string splits each char:", tea_varities)

# Reset list
tea_varities = ["black tea", "Green tea", "Oolong", "white"]
# Replace slice with a list — correct way
tea_varities[1:2] = ["lemon"]
print("Proper replacement:", tea_varities)

# Replace two items with one
tea_varities[1:3] = ["lemon"]
print("Two replaced with one:", tea_varities)

# Insert at index 1 without removing anything
tea_varities[1:1] = ["test", "test"]
print("After inserting:", tea_varities)

# Remove a slice
tea_varities[1:3] = []
print("After deletion:", tea_varities)

# Looping through the list (line by line)
for tea in tea_varities:
    print(tea)

# Looping with dash-separated print
for tea in tea_varities:
    print(tea, end="-")
print()  # new line

# Membership check
if "Oolong" in tea_varities:
    print("I have Oolong tea")

# Append "Oolang" (note the typo)
tea_varities.append("Oolang")

# Membership check again (still "Oolong", not "Oolang")
if "Oolong" in tea_varities:
    print("I have Oolong tea")  # won't print

# Remove "green" (will cause error if not found)
# tea_varities.remove("green")  # ❌ Error: not in list

# So check before removing
if "green" in tea_varities:
    tea_varities.remove("green")

# Insert "green" at index 1
tea_varities.insert(1, "green")

# Copy list
tea_varities_copy = tea_varities.copy()
print("Copied list:", tea_varities_copy)

# Append original list to its copy (nested list)
tea_varities_copy.append(tea_varities)
print("Nested list:", tea_varities_copy)

# List comprehension
squared_nums = [x**2 for x in range(10)]
print("Squared numbers:", squared_nums)

# Just printing range object
print("Range object:", range(10))  # shows: range(0, 10)
print("Converted to list:", list(range(10)))  # shows: actual list
