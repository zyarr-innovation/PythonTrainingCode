def simpleIntrest(principle, period, rate):
    return (principle * period * rate)/100
   
a = eval (input ("Enter the principle amount: "))
b = eval (input ("Enter the duration: "))
c = eval (input ("Enter the rate of intrest: "))
 
interestAmt= simpleIntrest (a,b,c)
print("The interest on amount: ", a, "is ", interestAmt)
