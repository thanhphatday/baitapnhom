m = str(input("Month Name (Capitalize the first letter): ")) 
if m=="April" or m == "June" or m == "September" or m == "November":
    print("30 days")
if m=="January" or m == "March" or m == "May" or m == "July" or m == "August" or m == "October" or m == "December":
    print("31 days")
if m=='February':
    print("28 or 29 days")
