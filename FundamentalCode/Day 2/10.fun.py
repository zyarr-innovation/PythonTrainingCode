def billCalculator(costOfPizza,numberOfPizza,tax):
    totalCost = costOfPizza  * numberOfPizza
    salestax = totalCost*tax/100
    totalBill = totalCost + salestax 
    return totalBill
   
a = eval (input ("Enter the cost of the burger: "))
b = eval (input ("Enter the number of burger: "))
#sales tex is 2%
c = 2 
totalamount = billCalculator (a,b,c)
print("Your bill is: " , totalamount)
