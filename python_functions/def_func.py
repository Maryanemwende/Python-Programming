#!/usr/bin/python3

#define your function

def calculate_my_age():
    name = "Maryane Mwende"
    year_of_birth = 1999
    age = 2023 - year_of_birth
    print("My name is {} and I am {} years old".format(name, age))

#Call your function
calculate_my_age()

#to be more practical , let's pass parameters to the function
#the parameters passed to the function are used to calculate the user's age
#parameters make it possible for the function to be utilised by anyone, anytime

def whats_my_age(my_name, year_of_birth, current_year):
    my_age = current_year - year_of_birth
    print("{} you are {} years old".format(my_name, my_age))

#calling the function
whats_my_age("Maryane Mwende", 1999, 2023) #here we have used positional arguments

#using keyword arguments
whats_my_age(current_year=2023, year_of_birth=1999, my_name="Maryane Mwende")
