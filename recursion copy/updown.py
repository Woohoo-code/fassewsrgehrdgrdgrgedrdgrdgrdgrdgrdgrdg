def countdown(number):
    print(number)
    if number > 0:
        countdown(number-1)


def countup(numberS,numberE):
    print(numberS)
    if numberS < numberE:
        countup(numberS+1, numberE)
countup(0,996)