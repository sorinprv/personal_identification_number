from datetime import date
from random import randint

from dictionaries_liste import S

sex = randint(1, 6)


def major(var):
    date = var.day, var.month, var.year - 18
    return date


major = major(date.today())
major = list(major)
print(major, type(major))


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


year_complete = int(year_complete((year(sex)))[0])

an_major = major[2]
an_cnp = year_complete
print(year_complete)
print(an_major > an_cnp)
"""daca e bun nu intra, daca nu e bun nu intra."""
new_an_cnp = 2006
while an_major < an_cnp:
    while new_an_cnp > an_major:
        def year_complete(var):
            year1 = (var[-4])
            year2 = (var[-3])
            year3 = str(randint(0, 9))
            year4 = str(randint(0, 9))

            year = year1 + year2 + year3 + year4
            year = int(year)
            year_cnp = year3 + year4
            return year, year_cnp

print(new_an_cnp)


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

# print(day())


# def date():
#     return f"{day()}/{month()}/{year_complete((year(sex)))[0]}\n" \
#            f"cnp: {sex}" \
#            f"{year_complete(year(sex))[1]}{month()}{day()}"
#
#
# print(date())
