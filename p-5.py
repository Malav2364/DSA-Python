year = int(input("Enter the year : "))
if (year % 100!=0 and year%4==0) or (year%400==0):
    print("Year is Leap year !")
else:
    print("Not a Leap Year")