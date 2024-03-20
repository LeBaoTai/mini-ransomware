from cryptography.fernet import Fernet
import os

def dec(filename, key):
  fernet = Fernet(key)
  with open(filename, "rb") as f:
    encrypted_data = f.read()
  decrypted_data = fernet.decrypt(encrypted_data)
  with open(filename[:-4], "wb") as f:
    f.write(decrypted_data)
  
  os.remove(filename)