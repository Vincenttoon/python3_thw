# More Variables and Printing
# Format Strings

name = 'Vincent'
age = 28
height = 69 # inches
weight = 205 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# combine different variables to create a new one

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# height and weight in different formats
height_in_cm = height * 2.54
lbs_in_kg = weight * 0.45

# round() to round floating integers
round(height_in_cm)
round(lbs_in_kg)

# example sentence using round & converted variables
print(f"Vincent is {round(height_in_cm)} centimeters tall")
print(f"Vincent is {round(lbs_in_kg)} kilograms heavy")

