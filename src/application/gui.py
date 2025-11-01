import tkinter as tk

from .gui_utils import set_size
from .calculator.calculator_frame import CalculatorFrame
from resources import resource_path

class Application(tk.Tk):
    _instance = None

    # Ensure only one instance exist
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Application, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Window Setup
        self.title("Aiden's Calculator")

        # Set the icon for the window
        icon = tk.PhotoImage(file = resource_path("images/calculator.png"))
        self.iconphoto(False, icon)

        set_size(window = self, width = 400, height = 600, center_screen = True)
        self.resizable(False, False)

        main_view = tk.Frame(self)
        main_view.pack(side = "top", fill = "both", expand = True)

        main_view.grid_rowconfigure(0, weight = 1)
        main_view.grid_columnconfigure(0, weight = 1)

        frame = CalculatorFrame(main_view)
        frame.grid(row = 0, column = 0, sticky = "nsew")

    def start(self):
        """Start the application."""
        self.mainloop()