from cryptography.fernet import Fernet

def ma_hoa_file(filename, key):
  fernet = Fernet(key)
  with open(filename, "rb") as f:
    file_data = f.read()
  encrypted_data = fernet.encrypt(file_data)
  with open(filename + ".enc", "wb") as f:
    f.write(encrypted_data)


key = Fernet.generate_key()
with open('./key.txt', 'w') as f:
  f.writelines(str(key))
filename = "./users.txt"

ma_hoa_file(filename, key)