# Question No 1.
# Get a score value from the user.
userScore = input("Give me a score value: \n")
print("User score (as string):", userScore)  # Correct variable name: userScore

# Convert to integer.
userScore_in_int = int(userScore)
print("User score (as integer):", userScore_in_int)

# Ask user's age and determine category.
age = input("Please provide me age: ")
age = int(age)
if age < 13:
    print("chai")
elif age <= 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("senior")


# Question No 2.
age = 22
day = "wednesday" 
price = 12 if age >= 18 else 8

# Correct indentation and use correct comparison operator.
if day == "wednesday":
    price = price - 2
    # Alternatively: price -= 2

print("Ticket price for you is $:", price)


# Question No 3.
score = 85
if score >= 101:
    print("You are not allowed to input grade greater than 100")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)                                              


# Question No 4.
fruit = "Banana"
color = "Yellow"
if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Nothing")


# Question No 5.
weather = "Sunny"
# Use '==' for comparisons, not '='.
if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"
else:
    activity = "Stay indoors"

print("Activity:", activity)


# Question No 6.
distance = 5
if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends you the transport:", transport)


# Question No 7.
order_size = "Medium"
extra_shot = True

# Use consistent variable name for coffee.
if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)


# Question No 8.
password = "Secure3P@ss"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is:", strength)


# Question No 9.
year = 2023

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
