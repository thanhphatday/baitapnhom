n= float
a= int(input("Human_years="))

if 0<a<=2:
    n= 10.5*a
    print("", a, "Human year(s)" "= ", n,"dog years")
if a>2:
    n= 21.0 + (a-2)*4
    print(" ", a, "Human years = ", n, "dog years")
else:
    print("Error!")