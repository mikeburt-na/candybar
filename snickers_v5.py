from tkinter import *
from datetime import datetime, timedelta

class FullScreenApp:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)  # Set fullscreen mode
        self.master.bind('<Escape>', self.exit_fullscreen)  # Bind Escape key to exit fullscreen

        # Create frames for each table
        self.frame_table1 = Frame(self.master, bg="black")
        self.frame_table1.grid(row=0, column=0, sticky="nsew")
        self.frame_table2 = Frame(self.master, bg="black")
        self.frame_table2.grid(row=1, column=0, sticky="nsew")

        # Configure grid weights to make both columns equally stretchable
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        # Create tables
        self.create_table_one_column()
        self.create_table_two_columns()

        self.update_time_passed()

    def create_table_one_column(self):
        #label1 = Label(self.frame_table1, text="One Column Table", font=('Helvetica', 16))
        #label1.pack(fill=BOTH, expand=True)

        self.twix = Label(self.frame_table1, text="------------- Our Anniversaries ------------", font=("Comic Sans MS", 32), bg="black", fg="white")
        self.twix.pack(fill=BOTH, expand=True)
        #self.twix.grid(row=0, column=0, sticky="nsew")

        # Add more labels or widgets for your one-column table as needed

    def create_table_two_columns(self):
        label1 = Label(self.frame_table2, text="--------------- When it all started    --------------", font=('Helvetica', 16), bg="black", fg="white")
        label1.grid(row=1, column=0, sticky="nsew")

        label2 = Label(self.frame_table2, text="February 23rd 2001", font=('Helvetica', 16), bg="black", fg="white")
        label2.grid(row=2, column=0, sticky="nsew")
        
        label3 = Label(self.frame_table2, text="-------------- We made it legal    ---------------", font=('Helvetica', 16), bg="black", fg="white")
        label3.grid(row=1, column=1, sticky="nsew")

        label4 = Label(self.frame_table2, text="June 21st 2003", font=('Helvetica', 16), bg="black", fg="white")
        label4.grid(row=2, column=1, sticky="nsew")

        label5 = Label(self.frame_table2, text="--------------------------------------------------", font=('Helvetica', 16), bg="black", fg="white")
        label5.grid(row=3, column=0, sticky="nsew")

        label6 = Label(self.frame_table2, text="--------------------------------------------------", font=('Helvetica', 16), bg="black", fg="white")
        label6.grid(row=3, column=1, sticky="nsew")

        label7 = Label(self.frame_table2, font=('Helvetica', 16), bg="black", fg="white")
        label7.grid(row=4, column=0, sticky="nsew")

        # Add more labels or widgets for your two-column table as needed

    def update_time_passed(self):
        # Date to compare against (Change this to your desired date)
        start_date = datetime(2001, 2, 23, 0, 0, 0)
        current_date = datetime.now()

        time_passed = current_date - start_date
        days_passed = time_passed.days
        hours_passed = time_passed.seconds // 3600
        seconds_passed = time_passed.seconds
        years_passed = time_passed.days // 365.25
        years_passed_int = "{} Years As of {}".format(int(years_passed),current_date)

        self.label7.config(text=years_passed_int)
        #self.days_label.config(text=days_passed)
        #self.hours_label.config(text=hours_passed)
        #self.seconds_label.config(text=seconds_passed)
        #self.time_label.config(text=time_passed)

        self.master.after(1000, self.update_time_passed)  # Update every hour (3600000 milliseconds)

    def exit_fullscreen(self, event):
        self.master.attributes('-fullscreen', False)  # Exit fullscreen mode

def main():
    root = Tk()
    app = FullScreenApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
