#!/usr/bin/python3

#This calclates your age

year_of_birth = input("Please input your year of birth: ")
month_of_birth = input("In which month were you born? Select (1 - 12): ")
day_of_birth = input("Input the day: ")

#another appproach to calculating the age
current_year = input("What is the current year? : ")

your_age = int(current_year) - int(year_of_birth)

#print it out
print(day_of_birth, "-", month_of_birth, "-", year_of_birth)
print(your_age)
