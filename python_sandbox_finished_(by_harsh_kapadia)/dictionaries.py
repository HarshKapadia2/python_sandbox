# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# key-value pairs
# create dict
person_1 = {
    'first_name': 'Selena',
    'middle_name': 'Marie',
    'last_name': 'Gomez',
    'age': 27
}

# use constructor
person_2 = dict(first_name = 'Lucas', middle_name = 'Cornelis', last_name = 'van Scheppingen', age = 43)

print(person_2, type(person_2))

# get a value
print(person_1['first_name'])
print(person_1.get('last_name'))

# add key value
person_1['song'] = 'Who Says'
print(person_1)

# get all keys
print(person_1.keys())
print(person_1.items())

# copy dict
person_3 = person_1.copy()
person_3['birth_place'] = 'Texas'
print(person_3)

# remove item
del person_3['birth_place']
person_3.pop('age')
print(person_3)

# clear dict (of all items)
person_3.clear()
print(person_3)

# get length
print(len(person_1))

# list of dict
people = [
    {
        'name': 'Selena Marie Gomez',
        'age': 27
    },
    {
        'name': 'Lucas Cornelis van Scheppingen',
        'age': 43
    },
    {
        'name': 'Felix Arvid Ulf Kjellberg',
        'age': 30
    }
]

print(people[0]['name'])