# Create a dictionary
chai_types = {"Masala": "spicy", "ginger": "zesty", "Green": "Mild"}
print(chai_types)

# Access values
print(chai_types["Masala"])        # 'spicy'
print(chai_types.get("ginger"))    # 'zesty'
print(chai_types.get("Gingery"))   # None (not in dictionary)

# Update value
chai_types["Green"] = "Fresh"
print("Updated 'Green':", chai_types)

# Loop over keys
for chai in chai_types:
    print("Key:", chai)

# Loop over keys with values
for chai in chai_types:
    print("Key-Value:", chai, chai_types[chai])

# Loop using .items()
for key, value in chai_types.items():
    print("With .items():", key, value)

# Membership test
if "Masala" in chai_types:
    print("I have masala tea")

# Length
print("Length:", len(chai_types))

# Add new key-value pair
chai_types["Earl Grey"] = "Citrus"
print("Added 'Earl Grey':", chai_types)

# Remove key 
chai_types.pop("ginger")

# Remove last inserted item
chai_types.popitem()

# Delete key
del chai_types["Green"]

# Copy dictionary
chai_types_copy = chai_types.copy()
print("Copied dict:", chai_types_copy)

# Nested dictionary
tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "zesty"
    },
    "Tea": {
        "Green": "Mild",
        "Black": "strong"
    }
}
print("Nested dict:", tea_shop)
print("chai category:", tea_shop["chai"])
print("Ginger tea:", tea_shop["chai"]["Ginger"])

# Dictionary comprehension
squard_num = {x: x**2 for x in range(6)}
print("Squared numbers:", squard_num)

# Creating a dictionary from keys with default value
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print("New dict with default values:", new_dict)
``