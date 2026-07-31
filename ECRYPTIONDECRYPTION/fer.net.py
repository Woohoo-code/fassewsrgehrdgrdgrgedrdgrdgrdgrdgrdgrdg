from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
what = b"supersecure123uncrackable1.0"
token = f.encrypt(what)
print(token)
print(f"That meant: {what}")