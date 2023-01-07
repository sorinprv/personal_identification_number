import math

from cnp import constant, cnp_test, cnp
from dictionaries_liste import alfabet, S, AA, JJ

n = cnp
n1 = cnp_test

"""list string"""


def character_check(var):
    list = []
    for i in var:
        list.append(i)
    for a in alfabet:
        for b in var:
            if a == b:
                list.remove(b)
            elif a == b and a != b:
                print("you did something wrong -- def character_check")
    return list


# print(character_check(n)[0])

"""list integer"""


def character_check1(var):
    list_cnp = []
    for z in var:
        z = int(z)
        list_cnp.append(z)
    return list_cnp


def character_check2(var):
    r1 = character_check(var)
    r2 = character_check1(r1)
    return r2


# print(character_check(n))
# print(character_check(n1))


# print(character_check1(character_check(n)))
# print(character_check1(character_check(n1)))


def length_check(var):
    """repetare proces input"""
    if len(character_check2(var)) == 13:
        return f"the cnp has a 13-digit number {character_check2(var)}"
    elif len(character_check2(var)) > 13:
        return f"cnp has extra characters {character_check2(var)}"
    elif len(character_check2(var)) < 13:
        return f"cnp has minus characters {character_check2(var)}"
    else:
        print("you did something wrong -- def length_check")


def gender(var):
    x = 0
    while x < 1:
        nr = var[x]
        x += 1
    nr = int(nr)

    if nr == 1:
        return S['1']
    elif nr == 2:
        return S['2']
    elif nr == 3:
        return S['3']
    elif nr == 4:
        return S['4']
    elif nr == 5:
        return S['5']
    elif nr == 6:
        return S['6']
    elif nr == 7:
        return S['7']
    elif nr == 8:
        return S['8']
    else:
        "altceva"
    return var


def an_nastere(var):
    var = S['1'][-4] + S['1'][-3] + var[1] + var[2]
    return var


def luna_nastere(var):
    var = var[3] + var[4]
    return var


def zi_nastere(var):
    var = var[5] + var[6]
    return var


def judet(var):
    var = var[7] + var[8]
    var = str(var)
    for i in JJ:
        if i == var:
            return JJ[i]
    var = AA[i]
    return var


def nastere(var):
    var = var[9] + var[10] + var[11]
    var = int(var)
    return var


def numar_siguranta(var):
    var = character_check1(var)
    security = var[-1]
    del var[-1]
    k = constant
    inmultire = []
    for i in range(0, len(var)):
        inmultire.append(var[i] * k[i])
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
            return "cnp corupt"
    elif s > 9:
        s = 1
        if s == security:
            return "cnp valid"
        elif s != security:
            return "cnp corupt"
    return var


def total(var):
    return (f"def 1: {character_check2(var)}\n"
            f"def 2: {length_check(var)}\n"
            f"def sex {gender(var)}\n"
            f"def an {an_nastere(var)}\n"
            f"def luna {luna_nastere(var)}\n"
            f"def zi nastere {zi_nastere(var)}\n"
            f"def judet {judet(var)}\n"
            f"def al catelea nascut {nastere(var)}\n"
            f"def siguranta {numar_siguranta(var)}\n")


print(total(cnp))
