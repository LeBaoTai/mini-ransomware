import tkinter as tk
from services.api_services import ApiService

RED_BG = '#A0153E'
WHITE = '#EEEDED'

def pay_now():
  key = ApiService.get_mac()
  

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
    self.geometry('800x500')
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

    # nut chuyen tien
    pay_btn = tk.Button(
      master=main_frame, 
      text='Pay Now', 
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
