#############
## Imports ##
#############
# Imports of various modules go at the top of a Python program.
# Importing a module does not result in any output.
import random

# Now you can write something like random.choice(["heads", "tails"])
# Like shorter names?
import random as rnd

# Now you can write something like rnd.choice(["heads", "tails"])
# Just want one function from a module?
from random import choice

# Now you can write: choice(["heads", "tails"])
# You can read more about modules at:
# https://realpython.com/python-modules-packages/

###########################
## Functions and Strings ##
###########################
def greet(greeting):
    return greeting + ", World!"


# Now you can write greet("Hello")
# Note that strings can be designated using single or double quotes
def greet(greeting="Hello"):
    return greeting + ", World!"


# Now you can write greet() and it will begin with "Hello" by default
# because of the default argument named above
def greet(greeting="Hello", audience="World"):
    return f"{greeting}, {audience}!"


# f-strings are a syntactic convenience, and highly addictive.
# prefixing your string with f allows you to interpolate defined
# variables, denoted by curly braces
# Note the multiple defined arguments in the function. You can
# name your arguments when calling the function. For instance,
# you can write greet(audience="Galaxy")

# Python has many "types"
# https://docs.python.org/3/library/stdtypes.html
a_number = 12
another_number = 7.1
a_string = "Some text"
another_string = "Some more text"
a_range = range(10)  # the numbers 0-9, in order
a_list = ["Some text", 14, another_number, "的", 1]

# Dictionaries (dicts) are a crucial part of Python
a_dict = {"a_key": "a_value", "first_name": "Sheila", "pi": 3.14159}

# Use this syntax to get the value of a specific key in a dict
archimedes_constant = a_dict["pi"]

# Lists, on the other hand, can be accessed by zero-based numeric index
a_lonely_number = a_list[4]

# This function demonstrates loops in Python.
def list_random_numbers(quantity, maximum=10):
    possible = range(maximum)
    for i in range(quantity):
        print(random.choice(possible))


# Read a file and print it to the console
def print_file(filename="sample.csv"):
    f = open(filename)
    contents = f.read()
    print(contents)
    f.close()


# Read a file and walk through it line by line
def walk_file(filename="sample.csv"):
    f = open(filename)
    for line in f:
        print(line, end="")
    f.close()


# Read a file, and write each line to a different file
# if that line contains the string "Teacher"
def write_new_file(infilename="sample.csv"):
    outfilename = f"tempfile{random.randint(1,9999)}.csv"
    infile = open(infilename, "r")
    outfile = open(outfilename, "w")
    for line in infile:
        if "Teacher" in line:
            outfile.write(line)
    infile.close()
    outfile.close()
    return outfilename
