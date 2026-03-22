import tkinter as tk
from controller.mock_controller import MockController
from gui.menu_bar import MenuBar
from gui.main_view import MainView

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scheduler")
        self.root.geometry("900x500")
        self.controller = MockController()
        
        # Global menu bar
        self.menu_bar = MenuBar(self.root, self.controller)
        # Current active view
        self.current_view = None
        self.switch_to_main()

    def switch_to_main(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = MainView(self.root, self.controller)
        self.current_view.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()