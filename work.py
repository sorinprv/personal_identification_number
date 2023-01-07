from cnp import cnp, cnp_test
from dictionaries_liste import alfabet

# def startprocess(self, rows, number):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             return (number, end="")
#             number -= 1
#     return ()
"""change elements from string to integer"""
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
                # else:
                #     print("nu e la fel")
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
            return ("you did something wrong -- def check")


user = Check_cnp(cnp_test)
# print(user.change())
# print(user.length_check())
