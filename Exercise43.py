denomination = int(input("Enter the denomination of the banknote: "))

if denomination == 1:
    name= ("George Washington")
    print(name)
elif denomination == 2:
    name = "Thomas Jefferson"
    print(name)
elif denomination == 5:
    name = "Abraham Lincoln"
    print(name)
elif denomination == 10:
    name = "Alexander Hamilton"
    print(name)
elif denomination == 20:
    name = "Andrew Jackson"
    print(name)
elif denomination == 50:
    name = "Ulysses S. Grant"
    print(name)
elif denomination == 100:
    name = "Benjamin Franklin"
else:
    print("Error: No such banknote exists.")
    

