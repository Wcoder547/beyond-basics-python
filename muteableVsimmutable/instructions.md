# Mutable vs Immutable Objects in Python

## What Are Objects in Python?

- Every variable in Python holds an instance of an object.
- There are two main types of objects:
  - Mutable
  - Immutable
- Each object has a unique ID.
- The object type is defined at runtime and cannot be changed.
- If the object is mutable, its internal state can be modified.

---

## Immutable Objects in Python

Immutable objects cannot be changed after creation.

**Examples of Immutable Types:**

- int
- float
- bool
- str
- tuple
- unicode

### Example 1: Tuple (Immutable)

```python
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4  # Error
```

**Error:**

```
TypeError: 'tuple' object does not support item assignment
```

### Example 2: String (Immutable)

```python
message = "Welcome to GeeksforGeeks"
message[0] = 'p'  # Error
```

**Error:**

```
TypeError: 'str' object does not support item assignment
```

---

## Mutable Objects in Python

Mutable objects can be changed after creation.

**Examples of Mutable Types:**

- list
- dict
- set
- custom classes

---

## Lists are Mutable

Lists allow modifications such as adding, removing, and changing elements.

### Example:

```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.insert(1, 5)
my_list.remove(2)
popped_element = my_list.pop(0)

print(my_list)
print(popped_element)
```

**Output:**

```
[5, 3, 4]
1
```

---

## Dictionaries are Mutable

You can modify key-value pairs.

### Example:

```python
my_dict = {"name": "Ram", "age": 25}
new_dict = my_dict
new_dict["age"] = 37

print(my_dict)
print(new_dict)
```

**Output:**

```
{'name': 'Ram', 'age': 37}
{'name': 'Ram', 'age': 37}
```

---

## Sets are Mutable

You can add or remove elements from a set.

### Example:

```python
my_set = {1, 2, 3}
new_set = my_set
new_set.add(4)

print(my_set)
print(new_set)
```

**Output:**

```
{1, 2, 3, 4}
{1, 2, 3, 4}
```

---

## Special Case: Tuple with Mutable Objects

Tuples are immutable, but if they contain a mutable item (like a list), that item can still be changed.

### Example:

```python
tup = ([3, 4, 5], 'myname')
tup[0].append(6)
print(tup)
```

**Output:**

```
([3, 4, 5, 6], 'myname')
```

---

## Summary

- Immutable objects: faster access, but cannot be changed directly.
- Mutable objects: can be modified easily.
- Use mutable types when you need to change or update values.
- Typically:

  - Primitive types (int, str, float) → Immutable
  - Container types (list, dict, set) → Mutable
