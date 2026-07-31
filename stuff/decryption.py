import string
import random
from spellchecker import SpellChecker


def crack(key, what):
    letter = []
    for i in range(26):
        letter.append(string.ascii_uppercase[i])
    alphabet = []
    for i in range(26):
        alphabet.append(string.ascii_uppercase[i])
    what = list(what)
    cipher = ""
    for k in range(key):
        letter.insert(0,letter.pop())
    for i in what:   
        j = alphabet.index(i)
        cipher = cipher+str(letter[j])

    return cipher
        
cracked = False
spell = SpellChecker("en")
word = input("Input cipher:  ")

i = 0 
word = word.split(" ")

options = []
for w in range(len(word)):
    i = 0
    temp = []
    while i < 26:
        i += 1            
        cr = crack(i, word[w])
        cr = cr.lower()
        if cr in spell.known([cr]):
            temp.append(cr)
    options.append(temp)
    

print(options, end=" ")
      
        
        

        


        






    


