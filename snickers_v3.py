from tkinter import *
from datetime import datetime, timedelta

class TableApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Mike and Bonnie - Anniversaries Timer')
        self.master.attributes("-fullscreen", True)

        # Create labels for headers
        headers = ['Name', 'Age', 'Occupation']
        for col, header in enumerate(headers):
            #label = Label(master, text=header, relief=RIDGE, width=15)
            label = Label(master, text=header, relief=RIDGE)
            label.grid(row=0, column=col)

        # Sample data for the table
        data = [
            ['John', 30, 'Engineer'],
            ['Alice', 25, 'Teacher'],
            ['Bob', 40, 'Doctor']
        ]

        # Display data in the table
        for row, row_data in enumerate(data, start=1):
            for col, cell_data in enumerate(row_data):
                #label = Label(master, text=str(cell_data), relief=RIDGE, width=15)
                label = Label(master, text=str(cell_data), relief=RIDGE)
                label.grid(row=row, column=col)

def main():
    root = Tk()
    app = TableApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
