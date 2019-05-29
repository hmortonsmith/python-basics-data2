# String types
# Strings are no more than a organised list/array of characters.
# You declare strings using quotes.

# Declaring a string
my_string = "I'm an amazing string"
my_string2 = "So am I!"
print(my_string)
print(type(my_string))

# Concatenation - joining of strings
print(my_string + ' - ' + my_string2)
print(my_string, '-', my_string2)
joint_string = my_string + ' - ' + my_string2
print(joint_string)

# Interpolation - putting something inside a string
age = 21
name = 'Anne'
example_text = f"{name} is {age} years old"
print(example_text)
example_text2 = f"{name} is {age * 2} years old"
print(example_text2)

# Useful methods (strip, Lower and Upper, length, count, capitalize, split)
example_text3 = '  HELLO'
print(example_text3)
print(example_text3.strip())
print(example_text3.count('H'))
print(len(example_text3))
print(len(example_text3.strip()))
print(example_text3.lower().strip())
print(example_text3.lower().strip().capitalize())

# Casting: changing things into strings or numbers

# Lastly




