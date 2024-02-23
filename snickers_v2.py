import tkinter as tk
from datetime import datetime

class TimePassedApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Time Passed Since a Certain Date")

        self.label = tk.Label(master, font=('Helvetica', 18))
        self.label.pack(pady=20)

        self.update_time_passed()

    def update_time_passed(self):
        # Date to compare against (Change this to your desired date)
        start_date = datetime(2023, 1, 1, 12, 0, 0)
        current_date = datetime.now()

        time_passed = current_date - start_date
        days_passed = time_passed.days
        hours_passed = time_passed.seconds // 3600

        #time_passed_str = days_passed +  " days and " +  hours_passed + " hours have passed since " + start_date.strftime('%Y-%m-%d %H:%M:%S')
        time_passed_str = days_passed
        self.label.config(text=time_passed_str)

        self.master.after(3600000, self.update_time_passed)  # Update every hour (3600000 milliseconds)

def main():
    root = tk.Tk()
    app = TimePassedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
