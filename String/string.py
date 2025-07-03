# Basic print
print("Hello world!")

chai = "masala chai"
print(chai)

chai = "ginger chai"
print(chai)

# Accessing characters and slices
first_char = chai[0]
print("First character:", first_char)

slice_chai = chai[0:6]
print("First 6 characters:", slice_chai)

slice_chai = chai[-1]
print("Last character:", slice_chai)

# Slicing a string
num_list = "0123456789"
print(num_list[:7])       # 0 to 6
print(num_list[3:])       # From index 3 to end
print(num_list[:])        # Full string
print(num_list[0:7:2])    # 0 to 6 with step 2
print(num_list[0:7:3])    # 0 to 6 with step 3

# String methods
print(chai.lower())       # Lowercase
print(chai.upper())       # Uppercase
print(chai.strip())       # Remove leading/trailing spaces
print(chai.replace("lemon", "ginger"))  # Doesn't find "lemon" in current string, so unchanged

# Reassign and use more methods
chai = "Lemon Ginger Masala Mint"
print(chai.split(", "))       # Only works with comma+space, returns entire string as 1 element
print(chai.find("Lemon"))     # Index of "Lemon"
print(chai.count("lemon"))    # Case-sensitive → 0

# String formatting
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} tea"
print(order.format(quantity, chai_type))

# List joining
chai_variety = ["Lemon", "Masala", "Ginger"]
print(" ".join(chai_variety))   # Space-separated
print("-".join(chai_variety))   # Hyphen-separated

# String length
print(len(chai))

# Fixed: for loop syntax (add colon at end)
for letter in chai:
    print(letter)

# Raw string
chai = r"Masala\chai"
print(chai)
