from cnp import cnp, cnp_test

cnp = list(cnp)
cnp_test = list(cnp_test)

# def startprocess(self, rows, number):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             return (number, end="")
#             number -= 1
#     return ()
"""change elements from string to integer"""


def change(cnp):
    list = []
    for i in cnp:
        i = int(i)
        list.append(i)
    return list


class cnp_reader:

    def check(self):
        # self.cnp = cnp
        if len(cnp) == 13:
            return (f"the cnp has a 13-digit number"
                    f"{change(cnp)}")
        elif len(cnp) > 13:
            return (f"cnp has extra characters {change(cnp)}")
        elif len(cnp) < 13:
            return (f"cnp has minus characters {change(cnp)}")
        else:
            return ("you did something wrong -- def check")

    def good(self):
        return ("all good")


abc = cnp_reader.check(cnp)
print(abc)
