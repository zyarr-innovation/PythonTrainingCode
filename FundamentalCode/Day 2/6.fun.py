
def posOrNeg(num):
    if num > 0:
        print("Number is positive: ", num)
    elif num < 0:
        print("Number is Negative: ", num)
    else:
        print("Number is zero: ", num)
 
numStr=input ("Enter the number: ")
num = int (numStr)
posOrNeg (num)
 
