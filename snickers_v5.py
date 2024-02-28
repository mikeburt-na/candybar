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
        self.label1 = Label(self.frame_table2, text="--------------- When it all Started --------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label1.grid(row=1, column=0, sticky="nsew")

        self.label2 = Label(self.frame_table2, text="February 23rd 2001", font=('Helvetica', 16), bg="black", fg="white")
        self.label2.grid(row=2, column=0, sticky="nsew")
        
        self.label3 = Label(self.frame_table2, text="-------------- We made it Legal ---------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label3.grid(row=1, column=1, sticky="nsew")

        self.label4 = Label(self.frame_table2, text="June 21st 2003", font=('Helvetica', 16), bg="black", fg="white")
        self.label4.grid(row=2, column=1, sticky="nsew")

        self.label5 = Label(self.frame_table2, text="--------------------------------------------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label5.grid(row=3, column=0, sticky="nsew")

        self.label6 = Label(self.frame_table2, text="--------------------------------------------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label6.grid(row=3, column=1, sticky="nsew")

        self.label7 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label7.grid(row=4, column=0, sticky="nsew")

        self.label71 = Label(self.frame_table2, text="-----------Next Dating Anniversary-----------", font=('Helvetica', 16), bg="black", fg="white")
        self.label71.grid(row=5, column=0, sticky="nsew")

        self.label8 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label8.grid(row=6, column=0, sticky="nsew")

        self.label9 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label9.grid(row=7, column=0, sticky="nsew")

        self.label10 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label10.grid(row=8, column=0, sticky="nsew")

        self.label11 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label11.grid(row=9, column=0, sticky="nsew")

        self.label122 = Label(self.frame_table2, text="-------------Count Down!!-------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label122.grid(row=10, column=0, sticky="nsew")

        self.label12 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label12.grid(row=11, column=0, sticky="nsew")


        self.label711 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label711.grid(row=4, column=1, sticky="nsew")

        self.label7115 = Label(self.frame_table2, text="-----------Next Wedding Anniversary-----------", font=('Helvetica', 16), bg="black", fg="white")
        self.label7115.grid(row=5, column=1, sticky="nsew")

        self.label712 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label712.grid(row=6, column=1, sticky="nsew")

        self.label713 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label713.grid(row=7, column=1, sticky="nsew")

        self.label714 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label714.grid(row=8, column=1, sticky="nsew")

        self.label715 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label715.grid(row=9, column=1, sticky="nsew")

        self.label7155 = Label(self.frame_table2, text="-------------Count Down!!-------------", font=('Helvetica', 16), bg="black", fg="white")
        self.label7155.grid(row=10, column=1, sticky="nsew")

        self.label716 = Label(self.frame_table2, font=('Helvetica', 14), bg="black", fg="white")
        self.label716.grid(row=11, column=1, sticky="nsew")

        # Add more labels or widgets for your two-column table as needed

    def update_time_passed(self):
        # Header
        current_date = datetime.now()
        current_year = current_date.year
        format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        # Dating Information
        dating_date = datetime(2001, 2, 23, 0, 0, 0)
        wed_date = datetime(2003, 6, 21, 0, 0, 0)
        # Dating Current
        dating_time_passed = current_date - dating_date
        dating_years_passed = dating_time_passed.days // 365.25
        dating_years_passed_int = "{} Years As of {}".format(int(dating_years_passed),format_date)
        # Dating Future
        #Check Year for accurate Delta
        dating_next_ann_check = datetime((current_year + 1), 2, 23, 0, 0, 0)
        dating_delta_check = dating_next_ann_check - current_date
        if dating_delta_check.days >= 365:
            dating_next_ann = datetime(current_year, 2, 23, 0, 0, 0)
            dating_delta = dating_next_ann - current_date
        else:
            dating_next_ann = datetime((current_year + 1), 2, 23, 0, 0, 0)
            dating_delta = dating_next_ann - current_date
        dating_next_year_days = dating_delta.days
        dating_next_year_days_str = "{} More Days".format(int(dating_next_year_days))
        dating_next_year_hours = dating_next_year_days * 24
        dating_next_year_hours_str = "{} More Hours".format(int(dating_next_year_hours))
        dating_next_year_min = dating_next_year_hours * 60
        dating_next_year_min_str = "{} More Minutes".format(int(dating_next_year_min))
        dating_next_year_sec = dating_next_year_min * 60
        dating_next_year_sec_str = "{} More Seconds".format(int(dating_next_year_sec))
        dating_next_year_cd = dating_delta
        dating_next_year_cd_str = "{}".format(dating_next_year_cd)

        # Dating Current
        wed_time_passed = current_date - wed_date
        wed_years_passed = wed_time_passed.days // 365.25
        wed_years_passed_int = "{} Years As of {}".format(int(wed_years_passed),format_date)

        # Wedding Future
        wed_next_ann = datetime((current_year + 1), 6, 21, 0, 0, 0)
        wed_delta = wed_next_ann - current_date
        wed_next_year_days = wed_delta.days
        wed_next_year_days_str = "{} More Days".format(int(wed_next_year_days))
        wed_next_year_hours = wed_next_year_days * 24
        wed_next_year_hours_str = "{} More Hours".format(int(wed_next_year_hours))
        wed_next_year_min = wed_next_year_hours * 60
        wed_next_year_min_str = "{} More Minutes".format(int(wed_next_year_min))
        wed_next_year_sec = wed_next_year_min * 60
        wed_next_year_sec_str = "{} More Seconds".format(int(wed_next_year_sec))
        wed_next_year_cd = wed_delta
        wed_next_year_cd_str = "{}".format(wed_next_year_cd)


        self.label7.config(text=dating_years_passed_int)
        self.label8.config(text=dating_next_year_days_str)
        self.label9.config(text=dating_next_year_hours_str)
        self.label10.config(text=dating_next_year_min_str)
        self.label11.config(text=dating_next_year_sec_str)
        self.label12.config(text=dating_next_year_cd_str)

        self.label711.config(text=wed_years_passed_int)
        self.label712.config(text=wed_next_year_days_str)
        self.label713.config(text=wed_next_year_hours_str)
        self.label714.config(text=wed_next_year_min_str)
        self.label715.config(text=wed_next_year_sec_str)
        self.label716.config(text=wed_next_year_cd_str)
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
