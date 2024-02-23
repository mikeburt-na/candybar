from tkinter import *
from datetime import datetime, timedelta

class TimePassedApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Time Passed Since a Certain Date")

        self.label = Label(master, font=('Helvetica', 18))
        self.label.pack(pady=20)

        self.update_time_passed()

    def update_time_passed(self):
        # Date to compare against (Change this to your desired date)
        start_date = datetime(2001, 2, 22, 0, 0, 0)
        current_date = datetime.now()

        time_passed = current_date - start_date
        days_passed = time_passed.days
        hours_passed = time_passed.seconds // 3600
        years_passed = time_passed.days // 364.25
        years_passed_int = int(years_passed)

        #time_passed_str = days_passed +  " days and " +  hours_passed + " hours have passed since " + start_date.strftime('%Y-%m-%d %H:%M:%S')
        #time_passed_str = days_passed
        time_passed_str = years_passed_int
        self.years_label.config(text=time_passed_str)
        self.time_label.config(text=time_passed)

        self.master.after(60000, self.update_time_passed)  # Update every hour (3600000 milliseconds)

def main():
    root = Tk()
    root.title('Mike and Bonnie - Anniversaries Timer')
    root.attributes("-fullscreen", True)

    twix = Label(root, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
    twix.pack(pady=20, ipadx=10, ipady=10)

    payday = Label(root, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
    payday.pack(pady=20, ipadx=10, ipady=10)
    app = TimePassedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
