from cnp import cnp_test
from dictionaries_liste import alfabet
from work import change


class Cnp_reader:
    def __init__(self, cnp):
        self.cnp = cnp

    def change(self):
        # self.cnp_test = cnp_test
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
        return list_cnp

    def length_check(self, cnp):
        self.cnp = change
        if len(change(cnp)) == 13:
            return (f"the cnp has a 13-digit number"
                    f"{change(cnp)}")
        elif len(change(cnp)) > 13:
            return (f"cnp has extra characters {change(cnp)}")
        elif len(change(cnp)) < 13:
            return (f"cnp has minus characters {change(cnp)}")
        else:
            return ("you did something wrong -- def check")


abc = Cnp_reader.length_check(cnp_test)
# abc = Cnp_reader.change(cnp_test)
print(abc)
