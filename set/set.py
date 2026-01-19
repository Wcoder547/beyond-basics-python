# Sets are used to store multiple items in a single variable.

# A set is a collection which is unordered, unchangeable*, and unindexed.No duplicate members.

# Once a set is created, you cannot change its items, but you can remove items and add new items.

from networkx import union


thisset = {"apple", "banana", "cherry"}
print(thisset)  # {'banana', 'cherry', 'apple'}

for x in thisset:
  print(x) 

thisset.add("orange")
print(thisset)  # {'banana', 'cherry', 'orange', 'apple'}

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # {'banana', 'cherry', 'orange', 'papaya', 'mango', 'apple', 'pineapple'}

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)  # {'banana', 'cherry', 'orange', 'papaya', 'mango', 'apple', 'kiwi', 'pineapple'}


thisset.remove("banana")
print(thisset)  # {'cherry', 'orange', 'papaya', 'mango', 'apple', 'kiwi', 'pineapple'}

thisset.discard("cherry")
print(thisset)  # {'orange', 'papaya', 'mango', 'apple', 'kiwi', 'pineapple'}

# differnce- remove raise an error if the item to remove does not exist, whereas discard does not raise an error.


x = thisset.pop()
print(x) # apple

print(thisset) # {'orange', 'papaya', 'mango', 'kiwi', 'pineapple'}\


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set3 = set1.union(set2)
myset = set1.union(set2, set3, set4)
print(set3) # {1, 2, 'b', 3, 'c', 'a'}
print(myset) # {1, 2, 3, 'bananas', 'apple', 'b', 'cherry', 'c', 'a'}

set5 = set1 & set2
print(set5) #set()

# frozenset is an immutable version of a set.

#Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.

x = frozenset({"apple", "banana", "cherry"})
print(x) #frozenset({'apple', 'cherry', 'banana'})
print(type(x)) # <class 'frozenset'>

# Method 	Shortcut 	Description 	
# copy() 	  	Returns a shallow copy 	
# difference() 	- 	Returns a new frozenset with the difference 	
# intersection() 	& 	Returns a new frozenset with the intersection 	
# isdisjoint() 	  	Returns whether two frozensets have an intersection 	
# issubset() 	<= / < 	Returns True if this frozenset is a (proper) subset of another 	
# issuperset() 	>= / > 	Returns True if this frozenset is a (proper) superset of another 	
# symmetric_difference() 	^ 	Returns a new frozenset with the symmetric differences 	
# union() 	| 	Returns a new frozenset containing the union






# ======================== Set Methods ========================
# Method 	Shortcut 	Description
# add() 	  	Adds an element to the set
# clear() 	  	Removes all the elements from the set
# copy() 	  	Returns a copy of the set
# difference() 	- 	Returns a set containing the difference between two or more sets
# difference_update() 	-= 	Removes the items in this set that are also included in another, specified set
# discard() 	  	Remove the specified item
# intersection() 	& 	Returns a set, that is the intersection of two other sets
# intersection_update() 	&= 	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() 	  	Returns whether two sets have a intersection or not
# issubset() 	<= 	Returns True if all items of this set is present in another set
#   	< 	Returns True if all items of this set is present in another, larger set
# issuperset() 	>= 	Returns True if all items of another set is present in this set
#   	> 	Returns True if all items of another, smaller set is present in this set
# pop() 	  	Removes an element from the set
# remove() 	  	Removes the specified element
# symmetric_difference() 	^ 	Returns a set with the symmetric differences of two sets
# symmetric_difference_update() 	^= 	Inserts the symmetric differences from this set and another
# union() 	| 	Return a set containing the union of sets
# update() 	|= 	Update the set with the union of this set and others