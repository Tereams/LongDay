import tkinter as tk
import calendar
from datetime import date


class CalendarView(tk.Frame):

    def __init__(self, parent, year, month, day_click_callback):
        super().__init__(parent)

        self.year = year
        self.month = month
        self.day_click_callback = day_click_callback

        self.cells = {}

        self.build_header()
        self.build_calendar()

    def build_header(self):

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, d in enumerate(days):
            label = tk.Label(self, text=d, font=("Arial", 10, "bold"))
            label.grid(row=0, column=col, padx=5, pady=5)

    def build_calendar(self):

        cal = calendar.Calendar(firstweekday=0)
        month_days = cal.monthdayscalendar(self.year, self.month)

        for row, week in enumerate(month_days):

            for col, day in enumerate(week):

                frame = tk.Frame(
                    self,
                    width=80,
                    height=60,
                    relief="ridge",
                    borderwidth=1
                )

                frame.grid(row=row + 1, column=col, padx=2, pady=2)
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
