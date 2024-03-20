from cryptography.fernet import Fernet
import os

class Encrypt():
  def __init__(self) -> None:
    pass

  def get_key(self):
    key = Fernet.generate_key(),
    return key

  def enc(self, filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as f:
      file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".enc", "wb") as f:
      f.write(encrypted_data)

    os.remove(filename)