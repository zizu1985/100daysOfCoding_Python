month=input("Please provide month name")

msg = "Hello Snow!"
if month == "January":
    msg = "Hello Snow!"
elif month == 'February':
    msg = "More Snow!"
elif month == 'March':
    msg = "No More Snow!"
elif month == 'April':
    msg = "Almost Golf Time"
elif month == 'May':
    msg = "Time to Golf"
elif month == "June":
    msg = "School's Out"
elif month == "July":
    msg = "Happy Fourth"
elif month == "August":
    msg = "Still Golfing"
elif month == "September":
    msg = "Welcome Back!"
elif month == "October":
    msg = "Fall Colors"
elif month == "November":
    msg = "Turkey Day"
elif month == "December":
    msg = "Merry Christmas!"
else:
    msg = "MONTH NOT FOUND"

print(msg)
