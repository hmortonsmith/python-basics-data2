list_evil_people = []

crazy_1 = {
    'name': 'Cruella de Ville',
    'occupation': 'Fashion designer',
    'address': 'Disney World',
    'skills': ['Fashion', 'laughing', 'design'],
}

crazy_2 = {
    'name': 'Ursula',
    'occupation': 'Under sea witch',
    'address': 'Mariana Trench',
    'skills': ['Swimming', 'Fishing'],
}

crazy_3 = {
    'name': 'Jafar',
    'occupation': 'Sorcerer',
    'address': 'The desert',
    'skills': ['Talking to parrots', 'laughing', 'beard trimming'],
}

crazy_4 = {
    'name': 'evil stepmother',
    'occupation': 'None',
    'address': "Cinderella's castle",
    'skills': ['Delegation'],
}

crazy_5 = {
    'name': 'Sheriff of Nottingham',
    'occupation': 'Sheriff',
    'address': 'Nottingham',
    'skills': ['Ruling', 'Feasting']
}

print(list_evil_people)
list_evil_people.append(crazy_1)
list_evil_people.append(crazy_2)
list_evil_people.append(crazy_3)
list_evil_people.append(crazy_4)
list_evil_people.append(crazy_5)
print(list_evil_people)

print(list_evil_people[2])
print(list_evil_people[2]['address'])
