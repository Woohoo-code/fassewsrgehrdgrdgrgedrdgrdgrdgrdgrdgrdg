from stack import stack
def parchecker():
    stacker = stack()

    pars = input("Enter your parenthsis         ")
    for i in pars:
        if i == "(" :
            stacker.add("(")
        elif stacker.getlen() == 0 or i == ")":
            if stacker.pop() == 0:
                print("Invalid")
                return 
    if stacker.pop() == 0:
        print("VALID")
    else:
            print("invalid")


parchecker()
