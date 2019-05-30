# Dictionaries work with Key Value Pairs
# They DO NOT use index. They use keys
# Keys are unique
# Dictionaries AKA --> Hashes or (confusingly) objects in JS

# Defining a Dictioanary
# use {}
# key: value
# where key can be string or number with colon (:) at the end.
# Value can be any object (arrays, dictionaries, strings, numbers...)

crazy_cruella_de_ville = {
    'name': 'Cruella de Ville',
    'occupation': 'Fashion designer',
    'address': 'Disney World',
    'skills': ['Fashion', 'laughing', 'design'],
    10: 'hello'

}

print(crazy_cruella_de_ville)
print(type(crazy_cruella_de_ville))

# How to access the dictionary - use the keys []
print(crazy_cruella_de_ville['occupation'])

# How to edit a value
# re-assign
# use key [] and re-assign
crazy_cruella_de_ville['door_number'] = 101
print(crazy_cruella_de_ville['door_number'])

# Accessing and manipulating using methods
crazy_cruella_de_ville['skills'].append('Business Skills')
print(crazy_cruella_de_ville['skills'])

# adding a new key: value
# same as editing - if it doesn't exist, it creates it

crazy_cruella_de_ville['favourite_colour'] = 'black and white'
print(crazy_cruella_de_ville['favourite_colour'])

# useful methods for dictionaries
# getting all the keys out (more useful than values - can get values from keys but not other way around)
keys = crazy_cruella_de_ville.keys()
print(keys)
# getting the values out
values = crazy_cruella_de_ville.values()
print(values)


# iterating over a hash/ dictionary:
# using for loop

print(crazy_cruella_de_ville.keys())

# when we iterate over a dictionary we get individual keys
for placeholder in crazy_cruella_de_ville:
    # this placeholder is each individual key
    print(placeholder)
    # put the placeholder in the dictionary to
    # extract individual values
    print(placeholder, ':', crazy_cruella_de_ville[placeholder])
