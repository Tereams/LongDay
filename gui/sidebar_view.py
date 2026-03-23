import tkinter as tk

class CollapsibleSection(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)

        self.expanded = True

        self.header = tk.Button(
            self,
            text=f"{title} ▼",
            anchor="w",
            command=self.toggle
        )
        self.header.pack(fill="x")

        self.body = tk.Frame(self)
        self.body.pack(fill="both", expand=True)

    def toggle(self):
        self.expanded = not self.expanded

        if self.expanded:
            self.body.pack(fill="both", expand=True)
            self.header.configure(text=self.header.cget("text").replace("▶", "▼"))
        else:
            self.body.pack_forget()
            self.header.configure(text=self.header.cget("text").replace("▼", "▶"))


class Sidebar(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack_propagate(False)

        # Task section
        self.task_section = CollapsibleSection(self, "Tasks")
        self.task_section.pack(fill="x", pady=5)

        # Constraint section
        self.constraint_section = CollapsibleSection(self, "Constraints")
        self.constraint_section.pack(fill="x", pady=5)

    def show_tasks(self, tasks):

        for w in self.task_section.body.winfo_children():
            w.destroy()

        for task in tasks:
            btn = tk.Button(
            self.task_section.body,
            text=f"{task.title} ({task.estimate_hours}h)",
            anchor="w",
            relief="flat",
            command=lambda t=task: self.on_task_clicked(t)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def set_task_click_handler(self, handler):
        self.on_task_clicked = handler

    def show_constraints(self, constraints):

        for w in self.constraint_section.body.winfo_children():
            w.destroy()

        for c in constraints:
            label = tk.Label(
                self.constraint_section.body,
                text=f"{c.type.value}: {c.start.strftime('%m-%d %H:%M')} → {c.end.strftime('%H:%M')}",
                anchor="w"
            )
            label.pack(fill="x", padx=5, pady=2)