bill=0
size=input("your order small medium large")
if (size=="small"):
    bill += 20
elif (size=="medium"):
    bill += 30
else:
    bill += 50
add_pepper=input("do you want to add_pepper? yes or no")
if (add_pepper == "yes" and size=="small"):
    bill += 20
elif (add_pepper == "yes" and size=="medium"):
    bill +=30
elif (add_pepper == "yes" and size=="medium"):
    bill +=40
else:
    bill=bill
add_cheese=input("do you want to add_cheese? yes or no")
if (add_cheese == "yes" and size=="small"):
    bill += 30
elif (add_cheese == "yes" and size=="medium"):
    bil +=40
elif (add_cheese == "yes" and size=="medium"):
    bil +=50
else:
    bill=bill
    print(bill)
