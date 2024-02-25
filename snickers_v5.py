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

    def create_table_one_column(self):
        #label1 = Label(self.frame_table1, text="One Column Table", font=('Helvetica', 16))
        #label1.pack(fill=BOTH, expand=True)

        self.twix = Label(self.frame_table1, text="------------------ Our Anniversaries ------------------", font=("Comic Sans MS", 32), bg="black", fg="white")
        #self.twix.pack(fill=BOTH, expand=True)
        self.twix.grid(row=0, column=0, sticky="nsew")

        # Add more labels or widgets for your one-column table as needed

    def create_table_two_columns(self):
        label1 = Label(self.frame_table2, text="Two Column Table - Column 1", font=('Helvetica', 16), bg="black", fg="white")
        label1.grid(row=0, column=0, sticky="nsew")
        
        label2 = Label(self.frame_table2, text="Two Column Table - Column 2", font=('Helvetica', 16), bg="black", fg="white")
        label2.grid(row=0, column=1, sticky="nsew")

        # Add more labels or widgets for your two-column table as needed

    def exit_fullscreen(self, event):
        self.master.attributes('-fullscreen', False)  # Exit fullscreen mode

def main():
    root = Tk()
    app = FullScreenApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
