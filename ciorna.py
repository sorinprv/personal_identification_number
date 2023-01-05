def startprocess(self, rows, number):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(number, end=" ")
            number -= 1
        print()


startprocess(1, 4, 10)
