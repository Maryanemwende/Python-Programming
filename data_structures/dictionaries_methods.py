#!/usr/bin/python3

#creating a dictionary - simple version
my_dict = {'name' : "Maryane", 'age' : 23, 'height' : 165}
print(my_dict)

#accessing the values
print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('height'))

#Iteration
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
for key in my_dict:
    print(key, my_dict[key])

#a dictionary of different types of immutable objs
dictionary = {
        'name' : "Mwesh",
        33 : 'Answer',
        (1, 2) : 'Coordinates',
        frozenset([3, 4, 5]) : 'Frozen Set',
        'details' : {
            'age' : 24,
            'home' : 'Wote'
            }
        }
print(dictionary['name'])
print(dictionary[33])
print(dictionary[(1, 2)])
print(dictionary[frozenset([3, 4, 5])])
print(dictionary['details']['home'])
