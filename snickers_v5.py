from tkinter import *
from datetime import datetime, timedelta

class TableApp:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)  # Set fullscreen mode
        self.master.bind('<Escape>', self.exit_fullscreen)  # Bind Escape key to exit fullscreen

        # Create table with one column
        self.create_table_one_column()

        # Create table with two columns
        self.create_table_two_columns()

    def create_table_one_column(self):
        table_frame = Frame(self.master)
        table_frame.grid(row=0, column=0, sticky=NSEW)
        self.master.columnconfigure(0, weight=1)  # Set column weight to 1 for resizing

        #label = Label(table_frame, text="One Column Table", font=('Helvetica', 16))
        #label.pack()

        self.twix = Label(table_frame, text="Mikey and Bonnie", font=("Helvetica", 42), bg="black", fg="white")
        self.twix.pack(pady=10, ipadx=10, ipady=10)

        # Add more labels or widgets for your one-column table as needed

    def create_table_two_columns(self):
        table_frame = Frame(self.master)
        table_frame.grid(row=0, column=1, sticky=NSEW)
        self.master.columnconfigure(1, weight=1)  # Set column weight to 1 for resizing

        label1 = Label(table_frame, text="Two Column Table - Column 1", font=('Helvetica', 16))
        label1.grid(row=0, column=0, sticky=NSEW)

        label2 = Label(table_frame, text="Two Column Table - Column 2", font=('Helvetica', 16))
        label2.grid(row=0, column=1, sticky=NSEW)

        # Add more labels or widgets for your two-column table as needed

    def exit_fullscreen(self, event):
        self.master.attributes('-fullscreen', False)  # Exit fullscreen mode

def main():
    root = Tk()
    app = TableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
