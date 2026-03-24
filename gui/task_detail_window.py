import tkinter as tk

class TaskDetailWindow(tk.Toplevel):

    def __init__(self, parent, task, on_save=None):
        super().__init__(parent)

        self.task = task
        self.on_save = on_save

        self.title("Task Detail")
        self.geometry("300x200")

        self.build_ui()

    def build_ui(self):

        tk.Label(self, text="Title:").pack(anchor="w")

        self.title_entry = tk.Entry(self)
        self.title_entry.insert(0, self.task.title)
        self.title_entry.pack(fill="x")

        tk.Label(self, text="Estimate Hours:").pack(anchor="w")

        self.hours_entry = tk.Entry(self)
        self.hours_entry.insert(0, str(self.task.estimate_hours))
        self.hours_entry.pack(fill="x")

        tk.Button(self, text="Save", command=self.save).pack(pady=10)

    def save(self):
        self.task.title = self.title_entry.get()
        self.task.estimate_hours = float(self.hours_entry.get())

        if self.on_save:
            self.on_save()

        self.destroy()