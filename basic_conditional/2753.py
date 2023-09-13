year = int(input())
is_leap_year = 0

if year % 400 == 0:
    is_leap_year = 1
elif year % 100 == 0:
    pass
elif year % 4 == 0:
    is_leap_year = 1
else:
    pass

print(is_leap_year)