from cnp import cnp_test
from dictionaries_liste import alfabet


class Check_cnp():
    def __init__(self, cnp_test):
        self.cnp_test = cnp_test
        # self.cnp = cnp

    def change(self):
        list = []
        for i in cnp_test:
            list.append(i)
        for a in alfabet:
            for b in list:
                if a == b:
                    list.remove(b)
        list_cnp = []
        for z in list:
            z = int(z)
            list_cnp.append(z)
        return (list_cnp)

    def length_check(self):
        if len(user.change()) == 13:
            return (f"the cnp has a 13-digit number"
                    f"{user.change()}")
        elif len(user.change()) > 13:
            return (f"cnp has extra characters {user.change()}")
        elif len(user.change()) < 13:
            return (f"cnp has minus characters {user.change()}")
        else:
            return ("you did something wrong -- def length_check")


user = Check_cnp(cnp_test)
# print(user.change())
# print(user.length_check())
