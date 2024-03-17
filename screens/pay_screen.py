import tkinter as tk
from home_screen import HomeScreen

class PayScreen(HomeScreen):
  def __init__(self, parent):
    super().__init__()
    self.title("Cửa sổ phụ")

    # Widget trong cửa sổ phụ
    self.label = tk.Label(self, text="Đây là cửa sổ phụ")
    self.label.pack()

    # Kích hoạt lại cửa sổ chính khi đóng cửa sổ phụ
    self.protocol("WM_DELETE_WINDOW", lambda: parent.state("normal"))