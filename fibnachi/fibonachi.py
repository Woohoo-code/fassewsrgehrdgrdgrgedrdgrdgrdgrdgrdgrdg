def fib(past):
    if past == 0:
        return 0
    elif past == 1:
        return 1
    else:
        return fib(past-1)+fib(past-2)

print(fib(996))
