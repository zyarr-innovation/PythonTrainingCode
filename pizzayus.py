number_of_pizza = eval(input("how many pizza do you want"))
cost_per_pizza = eval(input("how much does each pizza cost"))
subtotal =  number_of_pizza* cost_per_pizza
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total=subtotal + sales_tax
print("the total cost is $",total)
print("this includes $", subtotal,"for the pizza and")
print("$", sales_tax,"in sales tax") 