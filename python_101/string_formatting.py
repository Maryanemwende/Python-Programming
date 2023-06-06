#!/usr/bin/python3

#This program explores methods of formatting strings

high_school = input("Which HighSchool did you attend? : ")
city = input("In which city was your highschool located? : ")
year = int(input("When did you graduate from highschool? : "))

#let's print that out using the old formatting method
print("You attended %s in %s and finished in %d" %(high_school, city, year))
print()

#let's print using str.format method of formatting
print("You attended {} in {} and finished in {}".format(high_school, city, year))
print()

#An alternative to type casting
print("You attended {:s} in {:s} and finished in {:d}".format(high_school, city, year))
print()

#specifying the indices while printing the string
print("You attended {0} in {2} and finished in {1}".format(high_school, city, year))
print()

#using the newest method of string formatting f-string
print(f"You attended {high_school} in {city} and finished in {year}")
print()
print(F"You attended {high_school} in {city} and finished in {year}")

