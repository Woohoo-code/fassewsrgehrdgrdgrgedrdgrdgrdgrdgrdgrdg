from stack import stack
stackernum = stack()

numsandops = str(input("Enter your numbers and operations (SPACE SEPERATED):   "))
numsandops = numsandops.split(" ")
for i in range(len(numsandops)):
    if numsandops[i] == "+" or numsandops[i] == "-" or numsandops[i] == "*" or numsandops[i] == "/":
        if stackernum.getlen() > 1:
            num1 = stackernum.pop()
            num2 = stackernum.pop() 
            if numsandops[i] == "+":
                ans = num1+num2
                stackernum.add(ans)
            elif numsandops[i] == "-":
                ans = num2-num1
                stackernum.add(ans)
            elif numsandops[i] == "/":
                ans = num2/num1
                stackernum.add(ans)
            elif numsandops[i] == "*":
                
                ans = num1*num2
                stackernum.add(ans)
    else: 
        stackernum.add(int(numsandops[i]))
    
print(stackernum.peek())
