opener = input("file path: ")
mode = input("Mode ((w)rite aka append, (r)ead, r(e)set)")
open(opener, "r")
if mode == "w":
    add = input("what to add:   ")
    with open(opener, "a") as file:
        file.write(add)
elif mode == "e":
    with open(opener, "w") as file:
        file.write()
elif mode == "r":
    with open(opener, "r") as file:
        print(file.read())
else: 
    print("invalid mode") 
 
    



