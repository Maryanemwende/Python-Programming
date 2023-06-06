#!/usr/bin/python3

#This program explores a method (%) of formatting strings

High_School = input("Which HighSchool did you attend? : ")
city = input("In which city was your highschool located? : ")
year = int(input("When did you graduate from highschool? : "))

#let's print that out
print("You attended %s in %s and finished in %d" %(High_School, city, year))
