lister = ["bed","apple","den","bread","eggs","aardvark","far","head","line", "tafaf"]
#id = lister
#lister.append("")

for j in range(len(lister)-1):
    lister[j] =  lister[j].lower()
    for i in range(len(lister)-1):
        
        temp = lister[i]
        temp2 = lister[i+1]
        if temp>temp2:
            lister[i+1] = temp
            lister[i] = temp2
        

print(lister)


