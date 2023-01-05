# def startprocess(self, rows, number):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(number, end=" ")
#             number -= 1
#         print()
#
#
# startprocess(1, 4, 10)
from cnp import cnp_test
from dictionaries_liste import alfabet

list_cnp = []
list_cnp_test = []
# for i in cnp_test:
#     if i == alfabet[1]:
#         list_cnp.append(i)
#     else:
#         print("cnp valabil")
# print(list_cnp)
cnp_n = 0
cnp_test_n = 0
alfabet_n = 0

# while cnp_n == len(cnp):
#     while alfabet_n == len(alfabet):
#         if cnp[cnp_n] == alfabet[alfabet_n]:
#             cnp.pop[cnp_n]
#         alfabet_n += 1
#     cnp_n += 1
# print(cnp)


for i in cnp_test:
    list_cnp_test.append(i)
list_cnp_test = cnp_test
print(cnp_test)
while cnp_test_n != len(cnp_test):
    while alfabet_n != len(alfabet):
        if cnp_test[cnp_test_n] == alfabet[alfabet_n]:
            # cnp_test.pop(cnp_test_n)
            cnp_test.remove(cnp_test[cnp_test_n])
        alfabet_n += 1
    cnp_test_n += 1
print(cnp_test, len(cnp_test))
