
def leapYear(year):
    if year % 4 == 0:
        print("Leap year: ", year)
    else:
        print("Not a leap year: ", year)
 
numStr=input ("Enter the year ")
year = int (numStr)
leapYear (year)
 
