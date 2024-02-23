from tkinter import *
from datetime import datetime, timedelta

class TimePassedApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Mike and Bonnie - Anniversaries Timer')
        self.master.attributes("-fullscreen", True)

#   Header - Static Label
        self.twix = Label(master, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
        self.twix.pack(pady=20, ipadx=10, ipady=10)

        self.payday = Label(master, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
        self.payday.pack(pady=20, ipadx=10, ipady=10)

#   Dynamic Values
        self.time_label = Label(master, font=('Helvetica', 22))
        self.time_label.pack(pady=20)

        self.years_label = Label(master, font=('Helvetica', 22))
        self.years_label.pack(pady=20)

        self.days_label = Label(master, font=('Helvetica', 22))
        self.days_label.pack(pady=20)

        self.hours_label = Label(master, font=('Helvetica', 22))
        self.hours_label.pack(pady=20)

#   Static Values
        

        self.update_time_passed()

    def update_time_passed(self):
        # Date to compare against (Change this to your desired date)
        start_date = datetime(2001, 2, 21, 0, 0, 0)
        current_date = datetime.now()

        time_passed = current_date - start_date
        days_passed = time_passed.days
        hours_passed = time_passed.seconds // 3600
        years_passed = time_passed.days // 364.25
        years_passed_int = "{} Years Since we Fell Asleep On the Couch ".format(int(years_passed))

        self.years_label.config(text=years_passed_int)
        self.days_label.config(text=days_passed)
        self.hours_label.config(text=hours_passed)
        self.time_label.config(text=time_passed)

        self.master.after(60000, self.update_time_passed)  # Update every hour (3600000 milliseconds)

def main():
    root = Tk()
    #root.title('Mike and Bonnie - Anniversaries Timer')
    #root.attributes("-fullscreen", True)

    #twix = Label(root, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
    #twix.pack(pady=20, ipadx=10, ipady=10)

    #payday = Label(root, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
    #payday.pack(pady=20, ipadx=10, ipady=10)
    app = TimePassedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
