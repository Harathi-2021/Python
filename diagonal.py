x=int(input("Enter the number"))
y=int(input("Enter the number"))
left=x//10*y%10
right=y%10*x//10
sum=left+right
print(f"{left}+{right}={sum}")