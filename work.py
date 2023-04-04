# import math
#
# from cnp import constant, cnp_test, cnp
# from dictionaries_liste import alfabet, S, AA, JJ
#
# n = 1
# a = cnp
# b = cnp_test
# """"""""""""""""""""""""""""test & check"""""""""""""""""""""""""""
# """list string"""
#
#
# def character_check(var):
#     alist = []
#     for i in var:
#         alist.append(i)
#     for asd in alfabet:
#         for bgt in alist:
#             if asd == bgt:
#                 alist.remove(bgt)
#     return alist
#
#
# """check list integer"""
#
#
# def character_conversion(var):
#     list_cnp = []
#     for i in character_check(var):
#         i = int(i)
#         list_cnp.append(i)
#     return list_cnp
#
#
# def character_check2(var):
#     r1 = character_check(var)
#     r2 = character_conversion(r1)
#     return r2
#
#
# """check if the cnp number has 13 characters"""
#
#
# def length_check(var):
#     """repetare proces input"""
#     if len(character_check(var)) == 13:
#         var_check = []
#         var = var_check
#         return f"the cnp has a 13-digit number {character_check(var)}"
#     elif len(character_check(var)) > 13:
#         return f"cnp has extra characters {character_check(var)}"
#     elif len(character_check(var)) < 13:
#         # while n != 0:
#         #     user = input("User here:")
#         #     if len(user) == 13:
#         #         break
#         #     elif user == '0':
#         #         break
#         return f"cnp has minus characters {character_check(var)}"
#
#     else:
#         return "you did something wrong -- def length_check"
#
#
# # """"""""""""""""""""""""""""work"""""""""""""""""""""""""""
#
# """gender"""
#
#
# def gender(var_check):
#     x = 0
#     while x < 1:
#         nr = var_check[x]
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
#     return var_check
#
#
# """year of birth"""
#
#
# def year_of_birth(var_check):
#     var_check = S['1'][-4] + S['1'][-3] + var_check[1] + var_check[2]
#     return var_check
#
#
# """birth month"""
#
#
# def birth_month(var_check):
#     var_check = var_check[3] + var_check[4]
#     return var_check
#
#
# """birthday"""
#
#
# def birthday(var_check):
#     var_check = var_check[5] + var_check[6]
#     return var_check
#
#
# """county & sector"""
#
#
# def county_sector(var_check):
#     var_check = var_check[7] + var_check[8]
#     var_check = str(var_check)
#     for i in JJ:
#         if i == var_check:
#             return JJ[i]
#     var_check = AA[i]
#     return var_check
#
#
# """it is noted which child you were born on that day"""
#
#
# def birth_number(var_check):
#     var_check = var_check[9] + var_check[10] + var_check[11]
#     var_check = int(var_check)
#     return var_check
#
#
# """safety number"""
#
#
# def safety_number(var_check):
#     var_check = character_conversion(var_check)
#     security = var_check[-1]
#     del var_check[-1]
#     k = constant
#     inmultire = []
#     for i in range(0, len(var_check)):
#         inmultire.append(var_check[i] * k[i])
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
#     return var_check
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
# print(total(a))
import math

from cnp import cnp_test, cnp, constant
from dictionaries_liste import alfabet, S, JJ, AA

n = 1
a = cnp
b = cnp_test


class Test:
    def __init__(self, code):
        self.code = code

    def character_check(self):
        list_character_check = []
        for i in self.code:
            list_character_check.append(i)
        for y in alfabet:
            for z in list_character_check:
                if y == z:
                    list_character_check.remove(z)
        return list_character_check

    """check list integer"""

    def character_conversion(self):
        list_cnp = []
        for i in self.character_check():
            i = int(i)
            list_cnp.append(i)
        return list_cnp

    def length_check(self):
        """repetare proces input"""
        if len(self.character_conversion()) == 13:
            return f"the cnp has a 13-digit number {self.character_conversion()}"
        elif len(self.character_conversion()) > 13:
            return f"cnp has extra characters {self.character_conversion()}"
        elif len(self.character_conversion()) < 13:
            return f"cnp has minus characters {self.character_conversion()}"
        else:
            return "you did something wrong -- def length_check"


classfirst = Test(a)
# print(classfirst.length_check())
cnp_number = classfirst.character_conversion()
""""""
code_check = classfirst.length_check()
# print(code_check)
""""""


class Analysis:
    def __init__(self, code_good):
        self.code_good = code_good

    """gender"""

    def gender(self):
        number_gender = cnp_number[0]
        number_gender = int(number_gender)
        if number_gender == 1:
            return S['1']
        elif number_gender == 2:
            return S['2']
        elif number_gender == 3:
            return S['3']
        elif number_gender == 4:
            return S['4']
        elif number_gender == 5:
            return S['5']
        elif number_gender == 6:
            return S['6']
        elif number_gender == 7:
            return S['7']
        elif number_gender == 8:
            return S['8']
        else:
            "you did something wrong -- def gender"
        return number_gender, "xgfzdfxgh"

    """year of birth"""

    def year_of_birth(self):
        return gender[-4] + gender[-3] + str(cnp_number[1]) + str(cnp_number[2])

    """birth month"""

    def birth_month(self):
        return cnp_number[3] + cnp_number[4]

    """birthday"""

    def birthday(self):
        return cnp_number[5] + cnp_number[6]

    """county & sector"""

    def county_sector(self):
        location = str(cnp_number[7]) + str(cnp_number[8])
        for i in JJ:
            if i == location:
                return JJ[i]
        location = AA[i]
        return location

    """it is noted which child you were born on that day"""

    def birth_number(self):
        number = cnp_number[9] + cnp_number[10] + cnp_number[11]
        number = int(number)
        return number

    """safety number"""

    def safety_number(self):
        security = cnp_number[-1]
        del cnp_number[-1]
        k = constant
        inmultire = []
        for i in range(0, len(cnp_number)):
            inmultire.append(cnp_number[i] * k[i])
        s = 0
        for i in inmultire:
            s = s + i
            s = s / 11
        s = (s - math.floor(s)) * 100
        s = math.floor(s)
        if s <= 9:
            """s=06 => s=6"""
            s = int(s)
            if s == security:
                return "cnp valid"
            elif s != security:
                return "corrupt cnp"
        elif s > 9:
            s = 1
            if s == security:
                return "cnp valid"
            elif s != security:
                return "corrupt cnp"


classsecond = Analysis(code_check)
gender = classsecond.gender()
# print("sexul")
# gender = classsecond.gender()
# print(gender)
# print("anul de nastere")
# year_of_birth = classsecond.year_of_birth()
# print(year_of_birth)
# print("luna")
# birth_month = classsecond.birth_month()
# print(birth_month)
# print("ziua")
# birthday = classsecond.birthday()
# print(birthday)
# print("locatie")
# county_sector = classsecond.county_sector()
# print(county_sector)
# print("al catelea nascut")
# birth_number = classsecond.birth_number()
# print(birth_number)
# print("securitate")
# safety_number = classsecond.safety_number()
# print(safety_number)
