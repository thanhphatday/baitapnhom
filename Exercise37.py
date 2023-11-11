numsides=int(input("enter the number of sides: "))
if numsides < 3:
    print("Invalid number of sides. Please enter a number between 3 and 10.")
elif numsides > 10:
    print("Invalid number of sides. Please enter a number between 3 and 10.")
elif numsides==3:
    print("the shape with 3 sides is called a triangle.")
elif numsides==4:
    print("The shape with 4 sides is called a quadrilateral.")
elif numsides == 5:
    print("The shape with 5 sides is called a pentagon.")
elif numsides == 6:
    print("The shape with 6 sides is called a hexagon.")
elif numsides == 7:
    print("The shape with 7 sides is called a heptagon.")
elif numsides == 8:
    print("The shape with 8 sides is called an octagon.")
elif numsides == 9:
    print("The shape with 9 sides is called a nonagon.")
elif numsides == 10:
    print("The shape with 10 sides is called a decagon.")
