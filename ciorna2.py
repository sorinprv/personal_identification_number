from cnp import cnp, cnp_test
from dictionaries_liste import alfabet, S

"""list string"""


def character_check(var):
    list = []
    for i in var:
        list.append(i)
    for a in alfabet:
        for b in list:
            if a == b:
                list.remove(b)
    return list


"""check list integer"""


def character_conversion(var):
    list_cnp = []
    for i in character_check(var):
        i = int(i)
        list_cnp.append(i)
    return list_cnp


"""check if the cnp number has 13 characters"""


def length_check(var):
    """repetare proces input"""
    if len(character_check(var)) == 13:
        return f"the cnp has a 13-digit number {character_check(var)}"
    elif len(character_check(var)) > 13:
        return f"cnp has extra characters {character_check(var)}"
    elif len(character_check(var)) < 13:
        return f"cnp has minus characters {character_check(var)}"
    else:
        return "you did something wrong -- def length_check"


"""gender"""


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
        "you did something wrong -- def gender"
    return var


a = cnp
b = cnp_test
print(character_check(b))
print(character_conversion(b))
print(length_check(b))
print(gender(a))
