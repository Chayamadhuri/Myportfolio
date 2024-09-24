import math
print("looking to split the cost of a group purchase?\nwelcome to our receipt calculator!\nwe will ask a few questions about your purchase(s)to calculate the total cost per person.")
price_all= eval(input("step1:please input the cost of each product.\n(note:Eliminate the 's' sign instead separate with a'+'.)"))
tax_p =float(input("step 2:what is the sales tax in your area?\n(note:Eliminate the '%' sign. )"))
tip_p=float(input("step 3: what percentage would like to give as a tip?\n(note:Eliminate  the '%' sign.)") )
split =float(input("step 4: how many people are you splitting the bill with?\n(note:if you are not splitting the bill with anyone,just type'1'. )"))
total_p =(price_all + (price_all*(tax_p/100.0))+(price_all*(tax_p/100.0)))
final_p=round(total_p,2)
print("the total cost per person is: $",final_p,".")