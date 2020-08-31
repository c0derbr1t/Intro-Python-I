"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
# 🛑 STOP 
# 🧠 UNDERSTAND
"""
- Research calendars with the link given.
- What format do we want the calendar to be in
"""
# 🧩 PLAN
"""
- set up variables
  - get current date, and transform into strings for year and month
- make function
  - default args for year and month, dynamically set to current year and month
  - If no input is given:
    - print out a text based calendar, starting with Sunday (since we are in the US)
    - use current year and month
  - If one input is given:
    - print out a text based calendar, starting with Sunday
    - Assume input is month, use current year and input
  - If two inputs are given:
    - print out a text based calendar, starting with Sunday
    - Assume first input is year, and second is month, use the inputs for year and month.
  - Add error checking
"""
# 💫 EXECUTE
import sys
import calendar
from datetime import datetime, date

## Current Date Variables
current_date = str(date.today())
split_date = current_date.split("-")
current_year = int(split_date[0])
current_month = int(split_date[1])
current_day = int(split_date[2])

def print_calendar(year = current_year, month = current_month):
  text_cal = calendar.TextCalendar(6)
  print(text_cal.formatmonth(year, month))

# Arguments & Run
if len(sys.argv) == 3:
  if sys.argv[1].isdigit() and sys.argv[2].isdigit():
    if int(sys.argv[2]) >= 1 and int(sys.argv[2]) <= 12:
      print_calendar(int(sys.argv[1]), int(sys.argv[2]))
    else:
      print("Invalid parameter. Please enter a month between 1 and 12.")
  else:
    print("Invalid parameters. Please enter numbers such as YYYY and M or MM.")
elif len(sys.argv) == 2:
  if sys.argv[1].isdigit():
    if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 12:
      print_calendar(current_year, int(sys.argv[1]))
    else:
      print("Invalid parameter. Please enter a month between 1 and 12.")
  else:
    print("Invalid parameters. Please enter numbers such as M or MM.")
else:
  print_calendar()

# 🤯 REFLECT
"""
- The program works well.
- I could refactor so it takes less lines to get the current date values.
- I could expand to print the current day as well.
- I could add another parameter that takes into account the starting week day.
- I could add bounds to the year to keep it realistic. (currently works with year 0 lol)
"""