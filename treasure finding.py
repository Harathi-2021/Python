direction = str(input("Enter the direction left or right:"))

if direction == 'left':
    lake = input("your in island there is a lake do you want to type  wait or swim")
    if (lake == 'swim'):
        print("you are now safe")
        color = str(input("Enter the color"))
        if color == 'yellow':
            print("you win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")

