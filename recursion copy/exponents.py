def exponents(num, power):
    if power == 0:
        return 1
    else:
        return exponents(num, power-1)*num
    
print(exponents(2,3))