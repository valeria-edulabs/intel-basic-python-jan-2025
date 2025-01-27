# Exercise:
#
# You are given a list of birthdays as strings in the format "YYYY-MM-DD". Write a Python function that analyzes this list and returns the day of the week and the month with the most birthdays.
#
# The function should take one argument: a list of birthday strings.
# The function should return a tuple containing two strings:
# The day of the week with the most birthdays (e.g., "Monday").
# The month with the most birthdays (e.g., "May").
# In case of ties, return any of the most frequent days/months.

def bday_stats(bdays):
    # your implementation here
    pass

bdays = [
  "1990-05-15", "1985-08-21", "1995-05-10", "1992-08-18", "1988-05-03",
  "2001-08-05", "1998-05-22", "1987-08-11", "1993-05-08", "1999-08-29"
]
day, month = bday_stats(bdays)
print(f"Day with most birthdays: {day}")
print(f"Month with most birthdays: {month}")


# Expected Output:
#
# Day with most birthdays: Tuesday
# Month with most birthdays: May







