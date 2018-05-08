#Isaiah Frey
#Leap Year Checker program
#This program allows the user to enter a leap year and returns if it is
#a leap year or not

while (True):
    while (True):
        try:
            year = int(input("What year would you like to see if it is a leap year? "))
        except ValueError:
            print("Please enter a year")
        else:
            break
    if (year%4 == 0):
        if ((year%100 != 0) or (year%400 == 0)):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is not a leap year.")
