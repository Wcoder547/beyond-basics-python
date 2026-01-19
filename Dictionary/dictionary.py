# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

chai_types = {"Masala": "spicy", "ginger": "zesty", "Green": "Mild"}
print(chai_types)


print(chai_types["Masala"])        # 'spicy'
print(chai_types.get("ginger"))    # 'zesty'
print(chai_types.get("Gingery"))   # None (not in dictionary)


chai_types["Green"] = "Fresh"
print("Updated 'Green':", chai_types) # {'Masala': 'spicy', 'ginger': 'zesty', 'Green': 'Fresh'}


for chai in chai_types:
    print("Key:", chai)

for chai in chai_types:
    print("Key-Value:", chai, chai_types[chai])

for key, value in chai_types.items():
    print("With .items():", key, value)


if "Masala" in chai_types:
    print("I have masala tea")


print("Length:", len(chai_types))


chai_types["Earl Grey"] = "Citrus"
print("Added 'Earl Grey':", chai_types)


chai_types.pop("ginger")


chai_types.popitem()


del chai_types["Green"]


chai_types_copy = chai_types.copy()
print("Copied dict:", chai_types_copy) #{'Masala': 'spicy'}


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
print("Nested dict:", tea_shop) # {'chai': {'Masala': 'Spicy', 'Ginger': 'zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'strong'}}
print("chai category:", tea_shop["chai"]) #{'Masala': 'Spicy', 'Ginger': 'zesty'}
print("Ginger tea:", tea_shop["chai"]["Ginger"]) # 'zesty'

# Dictionary comprehension
squard_num = {x: x**2 for x in range(6)}
print("Squared numbers:", squard_num) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print("New dict with default values:", new_dict) #{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}



====================== Dictionary Methods ======================
# Method 	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary