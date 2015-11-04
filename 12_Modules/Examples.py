import calendar

cal = calendar.TextCalendar()
cal.setfirstweekday(calendar.THURSDAY)

print(cal.pryear(2012))
