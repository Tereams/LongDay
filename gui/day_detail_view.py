import tkinter as tk

class DayDetailView(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.title = tk.Label(self, text="Select a day", font=("Arial", 14))
        self.title.pack(anchor="w", padx=10, pady=10)

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(fill="both", expand=True)

    def show_day(self, day, tasks):

        self.title.configure(text=str(day))

        for widget in self.list_frame.winfo_children():
            widget.destroy()

        for start, end, name in tasks:

            label = tk.Label(
                self.list_frame,
                text=f"{start} - {end}  {name}",
                anchor="w"
            )

            label.pack(fill="x", padx=10, pady=2)
