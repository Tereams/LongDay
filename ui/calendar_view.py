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


class MockController:

    def get_month_workload(self, year, month):

        return {
            3: 2,
            5: 6,
            8: 4,
            12: 7,
            15: 3,
            18: 5,
            20: 8,
            25: 1
        }

    def get_day_schedule(self, day):

        return [
            ("09:00", "11:00", "Task A"),
            ("13:00", "15:00", "Task B"),
            ("16:00", "17:00", "Task C"),
        ]


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Scheduler")
        self.root.geometry("900x500")

        self.controller = MockController()

        self.build_layout()

    def build_layout(self):

        left = tk.Frame(self.root)
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        right = tk.Frame(self.root, width=250)
        right.pack(side="right", fill="y")

        self.calendar = CalendarView(
            left,
            2026,
            3,
            self.on_day_selected
        )

        self.calendar.pack()

        self.detail = DayDetailView(right)
        self.detail.pack(fill="both", expand=True)

        workload = self.controller.get_month_workload(2026, 3)

        self.calendar.set_workload(workload)

    def on_day_selected(self, day):

        tasks = self.controller.get_day_schedule(day)

        self.detail.show_day(day, tasks)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()