import tkinter as tk

class TwoTablesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Two Tables")
        self.master.attributes("-fullscreen", True)

        # Create frame for the first table
        self.frame_table1 = tk.Frame(master, bg="lightgreen")
        self.frame_table1.grid(row=0, column=0, sticky="nsew")

        # Create frame for the second table
        self.frame_table2 = tk.Frame(master, bg="green")
        self.frame_table2.grid(row=1, column=0, sticky="nsew")

        # Configure grid weights to make both rows equally stretchable
        self.master.rowconfigure(0, weight=0)
        self.master.rowconfigure(1, weight=1)

        # Create widgets for the first table
        self.create_table_one_column()

        # Create widgets for the second table
        self.create_table_two_columns()

    def create_table_one_column(self):
        label1 = tk.Label(self.frame_table1, text="Table 1 - One Column", font=('Helvetica', 16))
        label1.pack()

        # Add more labels or widgets for your one-column table as needed

    def create_table_two_columns(self):
        label1 = tk.Label(self.frame_table2, text="Table 2 - Column 1", font=('Helvetica', 16), bg="black", fg="white")
        label1.grid(row=0, column=0)

        label2 = tk.Label(self.frame_table2, text="Table 2 - Column 2", font=('Helvetica', 16), bg="white", fg="black")
        label2.grid(row=0, column=1)

        # Add more labels or widgets for your two-column table as needed

def main():
    root = tk.Tk()
    app = TwoTablesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
