#!/usr/bin/python3

#creating a tuple
lang_tuple = ('French', 'Deutsche', 'Arabic', 'Swahili')
print(lang_tuple)

#Accessing elements
print(lang_tuple[2])

#Tuple Slicing
slice_tuple = lang_tuple[1:3]
print(slice_tuple)

#Tuple unpacking
a, b, c, d = lang_tuple
print(c)

#Tuple iteration
for language in lang_tuple:
    print(language)

#SETS
#creating a set
names_set = {'Maryane', 'Mbash', 'Mus', 'Jennie'}
print(names_set)

#test membership
print('Mbash' in names_set)

names2_set = {'Mwesh', 'Esther', 'Mbash', 'Joshua'}
print(names2_set)

#intersection method
print(names_set.intersection(names2_set))
print(names_set.difference(names2_set))
print(names_set.union(names2_set))
print(names_set.symmetric_difference(names2_set))

print()
names2_set.clear()
print(names2_set)
names_set.remove('Maryane')
print(names_set)
names_set.discard('Mbash')
print(names_set)
