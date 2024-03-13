try :
    width = float(input("enter the rectangle width : "))
    length = float(input("Enter the lenth of the rectangle : "))

    if width == length :
        exit("This is a square and not a rectangle!")

    area = width * length
    print(area)
except ValueError :
    print("Invalid!" + "\n" + "Please enter a nmber next time")