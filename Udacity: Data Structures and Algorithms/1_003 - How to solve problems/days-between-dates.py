def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True


def days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365


def days_in_months(year, last_month):
    if is_leap_year(year):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:last_month - 1]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:last_month - 1]


def days_between_dates(y1, m1, d1, y2, m2, d2):
    days_in_diff_years = sum(map(days_in_year, range(y1, y2)))
    days_date1 = d1 + sum(days_in_months(y1, m1))
    days_date2 = d2 + sum(days_in_months(y2, m2)) + days_in_diff_years
    return days_date2 - days_date1


print(days_between_dates(2020, 2, 27, 2020, 2, 27))  # 0
print(days_between_dates(2020, 2, 27, 2020, 2, 28))  # 1
print(days_between_dates(2020, 2, 27, 2020, 2, 29))  # 2
print(days_between_dates(2020, 2, 27, 2020, 3, 1))   # 3
print(days_between_dates(2019, 1, 1, 2020, 1, 1))    # 365
print(days_between_dates(2019, 2, 27, 2020, 2, 27))  # 365
print(days_between_dates(2019, 3, 27, 2020, 3, 27))  # 366
