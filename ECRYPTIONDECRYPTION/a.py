import string

def encrypt(word, key):
    while len(key) < len(word):
        key = key+key
    if len(key) > len(word):
        removedigits = abs(len(key)-len(word))
        key = key[:-removedigits]
    print(key)
    key = list(key)
    #removedigits = abs(len(key)-len(word))

    letter = []
    for i in range(26):
        letter.append(string.ascii_uppercase[i])
    word = list(word)
    print(word)
    cipher = ""
    for i in range(len(word)):
        num = abs((letter.index(key[i])-letter.index(word[i]))%26)-1
        print(num)
        cipher = cipher+letter[num]
        print(letter[num])
    return cipher

def decrypt(word, key):
    while len(key) < len(word):
        key = key+key
    if len(key) > len(word):
        removedigits = abs(len(key)-len(word))
        key = key[:-removedigits]
    print(key)
    key = list(key)
    #removedigits = abs(len(key)-len(word))

    letter = []
    for i in range(26):
        letter.append(string.ascii_uppercase[i])
    word = list(word)
    print(word)
    cipher = ""
    for i in range(len(word)):
        num = abs((letter.index(key[i])-letter.index(word[i]))%26)-1
        print(num)
        cipher = cipher+letter[num]

    return cipher
print(encrypt("WORD", "KEY"))

