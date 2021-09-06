choice=int(input("Enter the choice number 1:addtion 2:subtraction 3:multiplication 4:division"))

if choice==1:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=a+b
    print("Result=",c)
elif choice==2:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=a-b
    print("Result=",c)
elif choice==3:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=a*b
    print("Result=",c)
elif choice==4:
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=a/b
    print("Result=",c)
elif choice==5:
    exit()
else:
    print("wrong number")

