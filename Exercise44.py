month=input("Enter the month: ")
day=int(input("Enter the day: "))
if month=="January" and day==1:
    print("The holiday on January 1 is New Year's Day.")
elif month=="July" and day==1:
    print("The holiday on July 1 is Canada Day.")
elif month=="December" and day==25:
    print("The holiday on December 25 is Christmas Day.")
else:
    print("The entered month and day do not correspond to a fixed-date holiday.")
