# Functions are integral to programming.
# Functional programming may not include OO programming
# You define functions and call them. That is it

# Define and call
# Best practices
    # 1. 1 function per function
    # 2. You should only have one job per function, this makes it testable
    # 3. Your functions should return, and not print. (unless it is really meant to print)
        # This is again for testability

# Functions help to keep code dry
    # Don't
    # Repeat
    # Yourself

# Syntax
# def <name>(<arg1, arg2...>):
    # Indented block of code

# The function needs to be called to run the block of code
# Call a function by using its name and passing in parameters


def hello_person(f_name, l_name):
    result = 'Hello ' + f_name + ' ' + l_name
    return result


print(hello_person('Harry', 'Morton-Smith'))
