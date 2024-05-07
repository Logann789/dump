# 3.k
month = int(input())
day = int(input())

days_in_month = {
    1: 31,  # January
    2: 28,  # February 
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}

# Check if its a leap year
is_leap_year = False
if (2017 % 4 == 0 and 2017 % 100 != 0) or (2017 % 400 == 0):
    is_leap_year = True

# Adjust feb days if its's a leap year
if is_leap_year:
    days_in_month[2] = 29

# Check if the entered day exceeds the number of days in the month
if day >= days_in_month[month]:
    day = 1
    month += 1
    if month > 12:
        month = 1

else:
    day += 1

print(month)
print(day)