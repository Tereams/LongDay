import tkinter as tk
import calendar
from datetime import date


class CalendarView(tk.Frame):

    def __init__(self, parent, year, month, 
                 day_click_callback,
                 prev_callback,
                 next_callback):
        
        super().__init__(parent)

        self.year = year
        self.month = month
        self.day_click_callback = day_click_callback
        self.prev_callback = prev_callback
        self.next_callback = next_callback
        
        self.cells = {}
        for i in range(7):
            self.columnconfigure(i, weight=1)
        for i in range(8):  # header + weekday + 6 weeks
            self.rowconfigure(i, weight=1)

        self.build_header()
        self.build_calendar()

    def build_header(self):
        
        # month switch
        control_frame = tk.Frame(self)
        control_frame.grid(row=0, column=0, columnspan=7, sticky="ew")

        prev_btn = tk.Button(control_frame, text="<", command=self.prev_callback)
        prev_btn.pack(side="left")

        self.title_label = tk.Label(
            control_frame,
            text=f"{self.year}-{self.month}",
            font=("Arial", 12, "bold")
        )
        self.title_label.pack(side="left", expand=True)

        next_btn = tk.Button(control_frame, text=">", command=self.next_callback)
        next_btn.pack(side="right")

        # week day
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, d in enumerate(days):
            label = tk.Label(self, text=d, font=("Arial", 10, "bold"))
            label.grid(row=1, column=col, padx=5, pady=5, sticky="nsew")

    def build_calendar(self):

        cal = calendar.Calendar(firstweekday=0)
        month_days = cal.monthdayscalendar(self.year, self.month)

        for row, week in enumerate(month_days):
            for col, day in enumerate(week):
                frame = tk.Frame(
                    self,
                    relief="ridge",
                    borderwidth=1
                )
                frame.grid(row=row + 2, column=col, padx=2, pady=2, sticky="nsew")
                frame.grid_propagate(False)

                if day != 0:
                    label = tk.Label(frame, text=str(day))
                    label.pack(anchor="nw")
                    frame.bind(
                        "<Button-1>",
                        lambda e, d=day: self.on_day_clicked(d)
                    )
                    label.bind(
                        "<Button-1>",
                        lambda e, d=day: self.on_day_clicked(d)
                    )
                    self.cells[day] = frame

    def set_workload(self, workload_map):
        for day, hours in workload_map.items():
            if day not in self.cells:
                continue
            frame = self.cells[day]
            color = self.workload_color(hours)
            frame.configure(bg=color)
    def refresh(self, year, month):
        self.year = year
        self.month = month

        for widget in self.winfo_children():
            widget.destroy()

        self.cells.clear()

        self.build_header()
        self.build_calendar()

    def workload_color(self, hours):
        if hours == 0:
            return "#ffffff"
        if hours <= 2:
            return "#c6e48b"
        if hours <= 4:
            return "#7bc96f"
        if hours <= 6:
            return "#239a3b"
        return "#196127"

    def on_day_clicked(self, day):
        selected_date = date(self.year, self.month, day)
        if self.day_click_callback:
            self.day_click_callback(selected_date)
