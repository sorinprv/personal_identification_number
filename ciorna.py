from cnp import cnp
from dictionaries_liste import alfabet, S

q = cnp
"""character_check"""
list = []
for i in q:
    list.append(i)
for a in alfabet:
    for b in list:
        if a == b:
            list.remove(b)
list_cnp = []
for z in list:
    z = int(z)
    list_cnp.append(z)
print(list_cnp)

"""length_check"""
if len(list_cnp) == 13:
    print(f"the cnp has a 13-digit number{list_cnp}")
elif len(list_cnp) > 13:
    print(f"cnp has extra characters {list_cnp}")
elif len(list_cnp) < 13:
    print(f"cnp has minus characters {list_cnp}")
else:
    print("you did something wrong -- def length_check")

"""decode cnp gender"""
print(list)

if list[0] == '1':
    print(S['1'])
elif list[0] == '2':
    print(S['2'])
elif list[0] == '3':
    print(S['3'])
elif list[0] == '4':
    print(S['4'])
elif list[0] == '5':
    print(S['5'])
elif list[0] == '6':
    print(S['6'])
elif list[0] == '7':
    print(S['7'])
elif list[0] == '8':
    print(S['8'])
else:
    print("error decode cnp gender")
