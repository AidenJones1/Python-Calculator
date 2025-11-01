import tkinter as tk
from tkinter.messagebox import showerror

from ..gui_utils import visual_grid
from .display_label import DisplayLabel
from .calculator_utils import is_valid_expression, shunting_yard_algorithm, convert_to_tree, calculate

class CalculatorFrame(tk.Frame):
    def calculate_sequence(self):
        if self.display.in_entry_mode():
            expr = self.display.get_expression()

            if is_valid_expression(expr):
                postfix_expr = shunting_yard_algorithm(expr)
                root_node = convert_to_tree(postfix_expr)
                res = calculate(root_node)

                self.display.set_display(res)
                self.display.set_previous_answer(res)

            else:
                showerror("Invalid Syntax", "Invalid Syntx")

    _instance = None

    # Ensure only one instance exist
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CalculatorFrame, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, parent: tk.Frame):
        tk.Frame.__init__(self, parent)

        # Frame Configuration
        self.config(background = "grey")

        # Grid Configuration
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = "row")
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = "column")
        #visual_grid(self, rows = 6, cols = 4)

        # Display
        self.display = DisplayLabel(self)
        self.display.config(
            text = "",
            font = ("Arial", 15),
            anchor = "e",
            padx = 10)
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew", padx = 5, pady = 5)

        # Buttons
        buttons = ["", "", "C", "←", "^", "(", ")", "/", "7", "8", "9", "+", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "ANS", "="]
        for row in range(6):
            for column in range(4):
                button_text = buttons[row * 4 + column]

                button = tk.Button(self)
                button.config(
                    text = button_text,
                    font = ("Arial", 15))
                button.grid(row = row + 1, column = column, sticky = "nsew", padx = 1, pady = 1)

                # Button Functionality
                match button_text:
                    case "":
                        button.config(state = tk.DISABLED)

                    case "ANS":
                        button.config(command = lambda: self.display.display_previous_answer())

                    case "C":
                        button.config(command = lambda: self.display.clear())

                    case "←":
                        button.config(command = lambda: self.display.delete())

                    case "=":
                        button.config(command = lambda: self.calculate_sequence())

                    case _:
                        button.config(command = lambda char = button_text: self.display.add(char))