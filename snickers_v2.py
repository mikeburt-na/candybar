from tkinter import *
from datetime import datetime, timedelta

class TimePassedApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Mike and Bonnie - Anniversaries Timer')
        self.master.attributes("-fullscreen", True)

#   Header - Static Label
        self.twix = Label(master, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
        self.twix.pack(pady=10, ipadx=10, ipady=10)

        self.payday = Label(master, text="Anniversaries Timer", font=("Helvetica", 42), bg="black", fg="white")
        self.payday.pack(pady=10, ipadx=10, ipady=10)

#   Dynamic Values
        #self.years_label = Label(master, font=('Helvetica', 22))
        #self.years_label.pack(pady=10)

        #self.time_label = Label(master, font=('Helvetica', 22))
        #self.time_label.pack(pady=20)

        #self.days_label = Label(master, font=('Helvetica', 22))
        #self.days_label.pack(pady=10)

        #self.hours_label = Label(master, font=('Helvetica', 22))
        #self.hours_label.pack(pady=10)

        #self.seconds_label = Label(master, font=('Helvetica', 22))
        #self.seconds_label.pack(pady=10)
#   Static Values
        
#   Table Start
         # Create labels for headers
        headers = ['Name', 'Age', 'Occupation']
        for col, header in enumerate(headers):
            label = Label(master, text=header, relief=RIDGE, width=15)
            label.grid(row=0, column=col, sticky=NSEW)
            master.columnconfigure(col, weight=1)  # Set column weight to 1 for resizing

        # Sample data for the table
        data = [
            ['John', 30, 'Engineer'],
            ['Alice', 25, 'Teacher'],
            ['Bob', 40, 'Doctor']
        ]

        # Display data in the table
        for row, row_data in enumerate(data, start=1):
            for col, cell_data in enumerate(row_data):
                label = Label(master, text=str(cell_data), relief=RIDGE, width=15)
                label.grid(row=row, column=col, sticky=NSEW)
        

        self.update_time_passed()

    def update_time_passed(self):
        # Date to compare against (Change this to your desired date)
        start_date = datetime(2001, 2, 24, 0, 0, 0)
        current_date = datetime.now()

        time_passed = current_date - start_date
        days_passed = time_passed.days
        hours_passed = time_passed.seconds // 3600
        seconds_passed = time_passed.seconds
        years_passed = time_passed.days // 365.25
        years_passed_int = "{} Years Since we Fell Asleep On the Couch ".format(int(years_passed))

        self.years_label.config(text=years_passed_int)
        self.days_label.config(text=days_passed)
        self.hours_label.config(text=hours_passed)
        self.seconds_label.config(text=seconds_passed)
        #self.time_label.config(text=time_passed)

        self.master.after(1000, self.update_time_passed)  # Update every hour (3600000 milliseconds)

def main():
    root = Tk()
    app = TimePassedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
