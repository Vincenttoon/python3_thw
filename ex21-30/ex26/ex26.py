from sys import argv

script, filename = argv

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")  # Added a missing parenthesis
weight = input()

print(f"So, you're {age} old, {height} tall, and {weight} heavy.")


txt = open(filename)  # Corrected the variable name

print(f"Here's your file {filename}:")
print(txt.read())  # Corrected the variable name

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())  # Corrected the method name

print("Let's practice everything.")
print("You'd need to know 'bout escapes with \\ that do \nnewlines and \ttabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  # Corrected the quotation marks
print(poem)
print("--------------")  # Corrected the quotation marks

five = 10 - 2 + 3 - 6  # Added the missing value

print(f"This should be five: {five}")


def secret_formula(started):  # Added a colon
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100  # Corrected the operator
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # Corrected the variable names

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
print(
    "We'd have {} beans, {} jars, and {} crates.".format(*formula)
)  # Corrected the variable names

people = 20
cats = 30  # Corrected the variable name
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:  # Corrected the inequality
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:  # Added a colon
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:  # Added a colon
    print("People are less than or equal to dogs.")

if people == dogs:  # Corrected the equality check
    print("People are dogs.")
