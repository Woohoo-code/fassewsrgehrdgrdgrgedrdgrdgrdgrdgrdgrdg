
def multply(num1,num2):
    if num1 == 0 or num2 == 0:
        return 0
    else:       
        return multply(num1, num2-1)+num1

print(multply(4000,5))