#!/usr/bin/python3

#This program explores a method (%) of formatting strings

high_school = input("Which HighSchool did you attend? : ")
city = input("In which city was your highschool located? : ")
year = int(input("When did you graduate from highschool? : "))

#let's print that out using the old formatting method
print("You attended %s in %s and finished in %d" %(high_school, city, year))

#let's print using str.format method of formatting
print("You attended {} in {} and finished in {}".format(high_school, city, year))
