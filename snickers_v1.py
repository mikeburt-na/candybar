from tkinter import *
from datetime import datetime, timedelta

def count_up_from_date(start_date_str, interval_seconds=1):
    # Convert start_date_str to datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')

    # Define the interval
    interval = timedelta(seconds=interval_seconds)

    # Start counting
    current_date = start_date
    while True:
        print(current_date.strftime('%Y-%m-%d %H:%M:%S'))
        current_date += interval

root = Tk()
root.title('Mike and Bonnie - Anniversaries Timer')
#root.iconbitmap('Images/Brian01.bmp')
#root.geometry("720x480")
root.attributes("-fullscreen", True)

twix = Label(root, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
twix.pack(pady=20, ipadx=10, ipady=10)

payday = Label(root, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
payday.pack(pady=20, ipadx=10, ipady=10)

butterfinger = "2001-02-23 00:00:00"
snickers = "2003-06-21 00:00:00"

reeses = count_up_from_date(butterfinger)


milkyway = Label(root, text=reeses, font=("Helvetica", 42), bg="black", fg="white")
milkyway.pack(pady=20, ipadx=10, ipady=10)

root.mainloop()