import tkinter as tk
from datetime import datetime, timedelta

class DateTimeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Date and Time Display")

        self.current_time_label = tk.Label(master, font=('Helvetica', 24))
        self.current_time_label.pack(pady=20)

        self.upcoming_time_label = tk.Label(master, font=('Helvetica', 18))
        self.upcoming_time_label.pack(pady=10)

        self.update_time()

    def update_time(self):
        current_time = datetime.now()
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
        self.current_time_label.config(text=f"Current Time: {current_time_str}")

        upcoming_time = datetime(2024, 3, 1, 12, 0, 0)  # Change this to your desired upcoming date and time
        time_delta = upcoming_time - current_time
        self.upcoming_time_label.config(text=f"Time until {upcoming_time.strftime('%Y-%m-%d %H:%M:%S')}: {time_delta}")

        self.master.after(1000, self.update_time)  # Update every second

def main():
    root = tk.Tk()
    app = DateTimeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
