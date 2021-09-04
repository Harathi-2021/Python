choice = int(input("Enter the choice number"))
if choice>=1 and choice<=4:
    print("Enter two numbers")
    num1=int(input())
    num2=int(input())
    if choice==1:
       opr=num1+num2
       print("Result=",opr)
    elif choice==2:
       opr=num1-num2
       print("Result=",opr)
    elif choice==3:
       opr=num1*num2
       print("Result=",opr)
    elif choice==4:
       opr=num1/num2
       print("Result=",opr)
    elif choice==5:
       exit()
else:
    print("invalid number")
