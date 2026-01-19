# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.



tea_varities = ["black tea", "Green tea", "Oolong", "white"]
print(tea_varities)

print(tea_varities[0])    #black tea
print(tea_varities[1:3])  #['Green tea', 'Oolong']


tea_varities[1:2] = "Lemon"
print("Replacing with string splits each char:", tea_varities) # ['black tea', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'white']


tea_varities = ["black tea", "Green tea", "Oolong", "white"]
tea_varities[1:2] = ["lemon"]
print("Proper replacement:", tea_varities) # ['black tea', 'lemon', 'Oolong', 'white']


tea_varities[1:3] = ["herbal"]
print("Two replaced with one:", tea_varities) # ['black tea', 'herbal', 'white']


tea_varities[1:1] = ["test", "test"]
print("After inserting:", tea_varities) # ['black tea', 'test', 'test', 'herbal', 'white']


tea_varities[1:3] = []
print("After deletion:", tea_varities) # ['black tea', 'herbal', 'white']


for tea in tea_varities:
    print(tea)


for tea in tea_varities:
    print(tea, end="-")
print()  # for newline



if "Oolong" in tea_varities:
    print("I have Oolong tea")


tea_varities.append("Oolang")

if "Oolong" in tea_varities:
    print("I have Oolong tea") 


if "green" in tea_varities:
    tea_varities.remove("green")


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']
del thislist # deletes the entire list

tea_varities.insert(1, "green")

# Copy list
tea_varities_copy = tea_varities.copy()
print("Copied list:", tea_varities_copy) # ['black tea', 'green', 'herbal', 'white', 'Oolang']


tea_varities_copy.append(tea_varities)
print("Nested list:", tea_varities_copy) # ['black tea', 'green', 'herbal', 'white', 'Oolang', ['black tea', 'green', 'herbal', 'white', 'Oolang']]


squared_nums = [x**2 for x in range(10)]
print("Squared numbers:", squared_nums) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


print("Range object:", range(10))# range(0, 10)
print("Converted to list:", list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# ============================ List Methods in Python ============================

# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
