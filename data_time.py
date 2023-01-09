import calendar
from datetime import date
from random import randint

"""This page will not generate a date under the age of 18 regardless of the day/month/year we are in"""


def year_genaration(var):
    year = randint(1800, var - 18)
    return year


generate_year = year_genaration(date.today().year)


# print(generate_year)


def month_genaration():
    var = randint(1, 12)
    return var


# print(month_genaration())
def setting_number_of_days(year, month):
    return calendar.monthrange(year, month)


setting_number_of_days = setting_number_of_days(generate_year, month_genaration())
setting_number_of_days = list(setting_number_of_days)


# print(type(setting_number_of_days))


def day_genaration():
    return randint(1, setting_number_of_days[1])


# print(day_genaration())
def date_genaration():
    year = generate_year
    month = month_genaration()
    day = day_genaration()
    return day, month, year


print(date_genaration())
