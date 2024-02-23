from tkinter import *
from datetime import date

root = Tk()
root.title('Mike and Bonnie - Anniversaries Timer')
#root.iconbitmap('Images/Brian01.bmp')
#root.geometry("720x480")
root.attributes("-fullscreen", True)

twix = Label(root, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
twix.pack(pady=20, ipadx=10, ipady=10)

payday = Label(root, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
payday.pack(pady=20, ipadx=10, ipady=10)

root.mainloop()