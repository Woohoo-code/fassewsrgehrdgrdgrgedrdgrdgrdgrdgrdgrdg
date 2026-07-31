


inputed = input("Encode or decode (e/d):    ")



def encode(what, key):
    cipher = ""
    for i in range(len(what)):
        num = ord(what[i])
        num = num+key
        cipher = cipher+str(chr(num))
    return cipher
def decode(what,key):
    cipher = ""
    for i in range(len(what)):
        num = ord(what[i])
        num = num-key
        cipher = cipher+str(chr(num))
    return cipher


key = int(input("What should the key be:    "))
if key >= 1114111:
    temp=key//1114111
    key=key-temp*1114111
if inputed == "e":
    what = input("What to encode:   ")
    print(encode(what, key))
    
elif inputed == "d":
    what = input("What to decode:   ")
    print(decode(what, key))

    









