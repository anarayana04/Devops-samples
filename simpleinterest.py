#####Write a program for calculating simple interest##
Principle_amt = int(input("Enter Pinciple amount:"))
Interest_rate = int(input("Enter interest rate:"))
Total_time = int(input("Enter Time:"))
Total_interest = (Principle_amt * Interest_rate * Total_time)/100
print(Total_interest)