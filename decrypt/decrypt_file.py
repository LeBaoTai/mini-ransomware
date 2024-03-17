from cryptography.fernet import Fernet

def giai_ma_file(filename, key):
  fernet = Fernet(key)
  with open(filename, "rb") as f:
    encrypted_data = f.read()
  decrypted_data = fernet.decrypt(encrypted_data)
  with open(filename[:-4], "wb") as f:
    f.write(decrypted_data)

with open('./key.txt', 'r') as f:
  key = Fernet(f.read().encode('utf-8'))
  filename = "./users.txt.enc"
  giai_ma_file(filename, key)
