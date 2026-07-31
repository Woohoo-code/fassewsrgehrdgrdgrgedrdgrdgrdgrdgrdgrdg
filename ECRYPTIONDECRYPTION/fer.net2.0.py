import hashlib
import string
import random
from cryptography.fernet import Fernet
m = hashlib.sha256()
k = ""

key = Fernet.generate_key()
with open("a.txt", "w") as filer:
    filer.write(key.decode("utf-"))
w = Fernet(key)
for i in range(50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
    if i%12 == 11:
        k = ""
    for i in range(12):
        k = str(k)+random.choice(string.ascii_letters)
    k = k.encode()
    m.update(k)
    p = bytes(m.hexdigest(), "utf-8")
    print(w.encrypt(p))
1