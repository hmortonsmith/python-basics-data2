# Lists in Python
# Keep a list of objects ordered by INDEX

# To declare a list, use [] square brackets
# Seperate objects using commas

crazy_x_landlord = ['Jane', 'Mike', 'Cruella de Ville']
print(crazy_x_landlord)
print(type(crazy_x_landlord))


# How do we access a list?
# With the index.

print(crazy_x_landlord[1])
print(crazy_x_landlord[-1])

# Edit entry
crazy_x_landlord[1] = 'Mike Tyson'
print(crazy_x_landlord)

# Adding to a list - use .append()
# Add Yuriy to list
crazy_x_landlord.append('Yuriy')
print(crazy_x_landlord)

# How to remove something from a list - Use .pop()
# Remove Jane
crazy_x_landlord.pop([0])
print(crazy_x_landlord)
