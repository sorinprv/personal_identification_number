# import math
#
# from cnp import constant, cnp
# from dictionaries_liste import alfabet, S, AA, JJ
#
# """list string"""
#
#
# def character_check(var):
#     li = []
#     for i in var:
#         li.append(i)
#     for a in alfabet:
#         for b in var:
#             if a == b:
#                 li.remove(b)
#             elif a == b and a != b:
#                 print("you did something wrong -- def character_check")
#     return li
#
#
# """list integer"""
#
#
# def character_check1(var):
#     list_cnp = []
#     for z in var:
#         z = int(z)
#         list_cnp.append(z)
#     return list_cnp
#
#
# def character_check2(var):
#     r1 = character_check(var)
#     r2 = character_check1(r1)
#     return r2
#
#
# """check if the cnp number has 13 characters"""
#
#
# def length_check(var):
#     """repetare proces input"""
#     if len(character_check2(var)) == 13:
#         return f"the cnp has a 13-digit number {character_check2(var)}"
#     elif len(character_check2(var)) > 13:
#         return f"cnp has extra characters {character_check2(var)}"
#     elif len(character_check2(var)) < 13:
#         return f"cnp has minus characters {character_check2(var)}"
#     else:
#         return "you did something wrong -- def length_check"
#
#
# """gender"""
#
#
# def gender(var):
#     x = 0
#     while x < 1:
#         nr = var[x]
#         x += 1
#     nr = int(nr)
#
#     if nr == 1:
#         return S['1']
#     elif nr == 2:
#         return S['2']
#     elif nr == 3:
#         return S['3']
#     elif nr == 4:
#         return S['4']
#     elif nr == 5:
#         return S['5']
#     elif nr == 6:
#         return S['6']
#     elif nr == 7:
#         return S['7']
#     elif nr == 8:
#         return S['8']
#     else:
#         "you did something wrong -- def gender"
#     return var
#
#
# """year of birth"""
#
#
# def year_of_birth(var):
#     var = S['1'][-4] + S['1'][-3] + var[1] + var[2]
#     return var
#
#
# """birth month"""
#
#
# def birth_month(var):
#     var = var[3] + var[4]
#     return var
#
#
# """birthday"""
#
#
# def birthday(var):
#     var = var[5] + var[6]
#     return var
#
#
# """county & sector"""
#
#
# def county_sector(var):
#     var = var[7] + var[8]
#     var = str(var)
#     for i in JJ:
#         if i == var:
#             return JJ[i]
#     var = AA[i]
#     return var
#
#
# """it is noted which child you were born on that day"""
#
#
# def birth_number(var):
#     var = var[9] + var[10] + var[11]
#     var = int(var)
#     return var
#
#
# """safety number"""
#
#
# def safety_number(var):
#     var = character_check1(var)
#     security = var[-1]
#     del var[-1]
#     k = constant
#     inmultire = []
#     for i in range(0, len(var)):
#         inmultire.append(var[i] * k[i])
#     s = 0
#     for i in inmultire:
#         s = s + i
#         s = s / 11
#     s = (s - math.floor(s)) * 100
#     s = math.floor(s)
#     if s <= 9:
#         """s=06 => s=6"""
#         s = int(s)
#         if s == security:
#             return "cnp valid"
#         elif s != security:
#             return "corrupt cnp"
#     elif s > 9:
#         s = 1
#         if s == security:
#             return "cnp valid"
#         elif s != security:
#             return "corrupt cnp"
#     return var
#
#
# def total(var):
#     return (f"def check if the cnp number has 13 characters:    {length_check(var)}\n"
#             f"def gender:                                       {gender(var)}\n"
#             f"def year_of_birth:                                {year_of_birth(var)}\n"
#             f"def birth_month:                                  {birth_month(var)}\n"
#             f"def birthday:                                     {birthday(var)}\n"
#             f"def county_sector:                                {county_sector(var)}\n"
#             f"def birth_number:                                 {birth_number(var)}\n"
#             f"def safety_number:                                {safety_number(var)}\n")
#
#
# print(total(cnp))
import calendar
from datetime import date
from random import randint

in_this_moment = date.today()
print(f"in_this_moment {in_this_moment}")


def year_genaration(var):
    year = randint(1800, var - 18)
    return year


generate_year = year_genaration(in_this_moment.year)


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
# a = calendar.weekday(1970, 11, 28)
# print(a)
# """setat inceput de saptamana cu luni"""
# calendar.setfirstweekday(0)
#
# print(calendar.leapdays(1800, 2005))

d = 9
m = 1
y = 2005

if d > in_this_moment.day and m > in_this_moment.month and y >= in_this_moment.year - 18:
    print("e minor")
elif d == in_this_moment.day and m == in_this_moment.month and y == in_this_moment.year - 18:
    print("verifica ora")
else:
    print("e major")

d = randint(1, 10)
m = randint(1, 12)
y = randint(2004, 2005)
print(d, m, y)
while d > in_this_moment.day and m > in_this_moment.month and y >= in_this_moment.year - 18:
    print(date_genaration())

# date_genaration() == list(day_genaration())
print(type(date_genaration()))
import datetime

start = datetime.datetime.strptime("01-01-1800", "%d-%m-%Y")
end = datetime.datetime.strptime("06-01-1800", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

for date in date_generated:
    print(date.strftime("%d-%m-%Y"))
