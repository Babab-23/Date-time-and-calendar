from datetime import date,time,datetime
# calling the today
# function of date class
today= date.today()
now=datetime.now()
print("Today's date is",today)
print("\n Current Date and Time is",now)
#Printing date's components
print("\n Date components",today.year,today.month,today.day)