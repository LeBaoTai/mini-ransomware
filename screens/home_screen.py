import tkinter as tk
from pay_screen import *

class HomeScreen(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Cửa sổ chính")

    # Nút để mở cửa sổ phụ
    self.button = tk.Button(self, text="Mở cửa sổ phụ", command=self.open_child)
    self.button.pack()

  def open_child(self):
    # Vô hiệu hóa cửa sổ chính
    # self.withdraw()

    # Tạo cửa sổ phụ
    self.child = PayScreen(self)


my_app = HomeScreen()
my_app.mainloop()