from cryptography.fernet import Fernet
import services.get_files as get_files
import os

def get_key():
  key = Fernet.generate_key(),
  return key

def enc(filename, key):
  fernet = Fernet(key)
  with open(filename, "rb") as f:
    file_data = f.read()
  encrypted_data = fernet.encrypt(file_data)

  with open(filename + ".enc", "wb") as f:
    f.write(encrypted_data)

  get_files.insert_enc_file(filename=filename + '.enc')
  os.remove(filename)