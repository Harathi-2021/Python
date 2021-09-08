food = input("your order please veg or non veg")
if food == "veg":
    order = input("breakfast or lunch")
    if order == "breakfast":
        print("order please:")
        variety = input(" enter your choice idly,poori,chapathi")
        if variety == 'idly' or variety == 'poori' or variety == 'chapathi':
            print("order is confirmed wait for sometime to get", variety)
        else:
            print("out of stok")

    elif order == "lunch":
        print("order please:")
        variety = input("Enter your choice meals,sambar rice,curd rice,lemon rice")
        if variety == 'meals' or variety == "sambar rice" or variety == "curd rice" or variety == "lemon rice":
            print("your order is confirmed and you can wait for sometime to get", variety)
        else:
            print("out of stock")
    else:
        print("invalid")
else:
    if food == "nonveg":
        order = input("breakfast or lunch")
        if order == "breakfast":
            print("order please")
            variety = input("Enter your choice chicken dosa,chicken parota")
            if variety == "chicken dosa" or variety == "chicken parota":
                print("your order is confirfmed wait for sometime to get", variety)
            else:
                print("out of stock")
        elif order == "lunch":
            print("order please")
            variety = input("Enter the choice chicken biriyani,mutton biriyani")
            if variety == "chicken biriyani" or variety == "mutton biriyani":
                print("your order is confirmed abd you can wait for sometime to get", variety)
            else:
                print("out of stock")
    else:
        print(invalid)