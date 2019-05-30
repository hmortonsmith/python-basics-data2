# Lists in Python
# Keep a list of objects ordered by INDEX
# Lists AKA --> (confusingly) objects in JS

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
crazy_x_landlord.pop(0)
print(crazy_x_landlord)

# Lists can contain anything
combined_list = [1, '10', 'ten', True, crazy_x_landlord]
print(combined_list)

# List slicing
# Used to manage lists
print(combined_list[0:3])
print(combined_list[3:])
print(combined_list[:3])
# Skip slicing - uses :: and returns from the first index and skips however many you specified
print(combined_list[0::2])


# Tuple is immutable list
# Defined with ()
# Same methods but can't append tuple (immutable)
# Accessed via index
mortal_enemies = ('Hello Kitty', 'Sailor Moon', 'Iron Man', 'Eye-patch Morty')
print(type(mortal_enemies))
# Cannot re-assign an index, it breaks
# mortal_enemies[1] = 'Goku'
