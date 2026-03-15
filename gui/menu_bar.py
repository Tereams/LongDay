import tkinter as tk


class MenuBar(tk.Menu):

    def __init__(self, root, controller):
        super().__init__(root)

        self.root = root
        self.controller = controller

        root.config(menu=self)

        self.build_file_menu()
        self.build_view_menu()
        self.build_help_menu()

    def build_file_menu(self):

        file_menu = tk.Menu(self, tearoff=0)

        file_menu.add_command(
            label="New",
            command=self.controller.new_schedule
        )

        file_menu.add_command(
            label="Open",
            command=self.controller.open_schedule
        )

        file_menu.add_command(
            label="Save",
            command=self.controller.save_schedule
        )

        file_menu.add_separator()

        file_menu.add_command(
            label="Exit",
            command=self.root.quit
        )

        self.add_cascade(label="File", menu=file_menu)

    def build_view_menu(self):

        view_menu = tk.Menu(self, tearoff=0)

        view_menu.add_command(
            label="Month View",
            command=self.controller.show_month_view
        )

        view_menu.add_command(
            label="Week View",
            command=self.controller.show_week_view
        )

        view_menu.add_command(
            label="Day View",
            command=self.controller.show_day_view
        )

        self.add_cascade(label="View", menu=view_menu)

    def build_help_menu(self):

        help_menu = tk.Menu(self, tearoff=0)

        help_menu.add_command(
            label="About",
            command=self.controller.show_about
        )

        self.add_cascade(label="Help", menu=help_menu)