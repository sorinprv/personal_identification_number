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

    """gender"""

    def gender(self):
        number_gender = Test(self.code).character_conversion()[0]
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
        return number_gender

    """year of birth"""

    def year_of_birth(self):
        y = (Test(self.code).character_conversion()[1])
        y = str(y)
        z = (Test(self.code).character_conversion()[2])
        z = str(z)
        year = Test(self.code).gender()[-4] + Test(self.code).gender()[-3] + y + z
        return year

    """birth month"""

    def birth_month(self):
        return Test(self.code).character_conversion()[3] + Test(self.code).character_conversion()[4]

    """birthday"""

    def birthday(self):
        return Test(self.code).character_conversion()[5] + Test(self.code).character_conversion()[6]

    """county & sector"""

    def county_sector(self):
        location = str(Test(self.code).character_conversion()[7]) + str(Test(self.code).character_conversion()[8])
        for i in JJ:
            if i == location:
                return JJ[i]
        location = AA[i]
        return location

    """it is noted which child you were born on that day"""

    def birth_number(self):
        number = Test(self.code).character_conversion()[9] + Test(self.code).character_conversion()[10] + \
                 Test(self.code).character_conversion()[11]
        number = int(number)
        return number

    """safety number"""

    def safety_number(self):
        security = Test(self.code).character_conversion()[-1]
        del Test(self.code).character_conversion()[-1]
        k = constant
        inmultire = []
        for i in range(0, len(Test(self.code).character_conversion())):
            inmultire.append(Test(self.code).character_conversion()[i] * k[i])
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

    def output(self):
        return (f"def check if the cnp number has 13 characters:    {self.length_check()}\n"
                f"def gender:                                       {self.gender()}\n"
                f"def year_of_birth:                                {self.year_of_birth()}\n"
                f"def birth_month:                                  {self.birth_month()}\n"
                f"def birthday:                                     {self.birthday()}\n"
                f"def county_sector:                                {self.county_sector()}\n"
                f"def birth_number:                                 {self.birth_number()}\n"
                # f"def safety_number:                                {self.safety_number()}")
                )


print(Test(a).output())
