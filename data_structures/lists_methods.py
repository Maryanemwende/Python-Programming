#!/usr/bin/python3

#exploring methods that can be used on lists

rainbow_colours = ['red', 'orange', 'green', 'blue']
print(rainbow_colours)

#oh! I forgot yellow. Let's add it (insert)
rainbow_colours.insert(2, 'yellow')
print()
print(rainbow_colours)

#let's add indigo (append)
rainbow_colours.append('indigo')
print(rainbow_colours)

#change of mind, lets remove indigo (remove)
rainbow_colours.remove('indigo')
print(rainbow_colours)

#now lets add both indigo and violet to complete our rainbow(extend)
rainbow_colours.extend(['indigo', 'violet'])
print(rainbow_colours)

#let's try the pop method
rainbow_colours.pop(3)
print(rainbow_colours)

#How long is our list?(len method)
length = len(rainbow_colours)
print(length)

#let's reverse our list(reverse method)
rainbow_colours.reverse()
print(rainbow_colours)

#index method
index = rainbow_colours.index('yellow')
print(index)

#finally, let us try the count method
count = rainbow_colours.count('indigo')
print(count)

#let's create a list of numbers so we can use the sort method
nums = [3, 5, 7, 2, 6, 1, 4]
nums.sort()
print(nums)

print(min(nums))
print(max(nums))

for index, colours in enumerate(rainbow_colours):
    print(index, colours)

for index, colours in enumerate(rainbow_colours, start=1):
    print(index, colours)

for colours in rainbow_colours:
    print(colours)

#list into string
colours_str = ', '.join(rainbow_colours)
new_list = colours_str.split(' - ')
print(colours_str)
print(new_list)
