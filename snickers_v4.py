from tkinter import *
from datetime import datetime, timedelta

class TableApp:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen', True)  # Set fullscreen mode
        self.master.bind('<Escape>', self.exit_fullscreen)  # Bind Escape key to exit fullscreen

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

    def exit_fullscreen(self, event):
        self.master.attributes('-fullscreen', False)  # Exit fullscreen mode

def main():
    root = Tk()
    app = TableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
