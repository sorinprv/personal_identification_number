from datetime import date
from random import randint

from dictionaries_liste import S

current_date = date.today()
year_now = current_date.year

sex = randint(1, 6)


def year(var):
    if var == 1:
        return S['1']
    elif var == 2:
        return S['2']
    elif var == 3:
        return S['3']
    elif var == 4:
        return S['4']
    elif var == 5:
        return S['5']
    elif var == 6:
        return S['6']
    else:
        "you did something wrong -- def gender"
    return var


def year_complete(var):
    year1 = (var[-4])
    year2 = (var[-3])
    year3 = str(randint(0, 9))
    year4 = str(randint(0, 9))

    year = year1 + year2 + year3 + year4
    year = int(year)
    year_cnp = year3 + year4
    return year, year_cnp


print(year_complete((year(sex))))


def month():
    month1 = str(randint(0, 1))
    month2 = str(randint(0, 2))
    month = month1 + month2
    return month


def day():
    day1 = str(randint(0, 2))
    day2 = str(randint(0, 9))
    day = day1 + day2
    # day = str(randint(0, 28))
    return day


print(day())


def date():
    return f"{day()}/{month()}/{year_complete((year(sex)))[0]}\n" \
           f"cnp: {sex}" \
           f"{year_complete(year(sex))[1]}{month()}{day()}"


print(date())
