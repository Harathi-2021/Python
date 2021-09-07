amount=int(input("Enter the amount"))
tips=int(input("Enter the tips"))
discount=(tips/100)*amount
print(discount)
total_amount=discount+amount
print(int(total_amount))