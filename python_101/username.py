#!/usr/bin/python3

# A program that generates your username

first_name = "Maryane"
surname = "Musyoka"

#using slicing to join characters from both names

username = first_name[0:3] + '_' + surname[0:3]

print("Your cool username is: ", end=" ")
print(username)
