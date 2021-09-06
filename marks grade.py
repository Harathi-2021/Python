mark=int(input("Enter the marks"))

if mark>=90 and mark<=100:
    print("A grade")
elif mark>=80 and mark<=89:
    print("B grade")
elif mark>=70 and mark<=79:
    print("c grade")
elif mark>=60 and mark<=69:
    print("D grade")
elif mark>=50 and mark<=59:
    print("E grade")
elif mark>=0 and mark<=49:
    print("fail")
else:
    print("fake input")