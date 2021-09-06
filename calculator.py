choice=int(input("Enter the choice number 1:addtion 2:subtraction 3:multiplication 4:division"))
a=int(input("Enter the number"))
b=int(input("enter the number"))
if choice==1:
    c=a+b
    print("Result=",c)
elif choice==2:
    c=a-b
    print("Result=",c)
elif choice==3:
    c=a*b
    print("Result=",c)
elif choice==4:
    c=a/b
    print("Result=",c)
elif choice==5:
    exit()
else:
    print("wrong number")

