def crypt(word, key):
    while len(key) < len(word):
        key = key+key
        if len(key) > len(word):
            removedigits = abs(len(key)-len(word))
            key = key[:-removedigits]
    test = word.encode("utf-8")
    bytese = bytearray(test)
    key = key.encode("utf-8")
    key = bytearray(key)
    cipher = bytearray()
    for byte in range(len(bytese)):
        q = bytese[byte]
        t = q^key[byte]
        cipher.append(t)
        print(cipher)
    cipher = cipher.decode()
    return cipher

    

print(crypt("","iieasfhishfiusehfihfsihesiuhfieshfiushfi"))
