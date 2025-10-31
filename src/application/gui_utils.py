import tkinter as tk

def set_size(window: tk.Tk, width: int, height: int, center_screen: bool = True):
    """Set window size and determine whether to start it center screen."""
    if center_screen:
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")

    else:
        window.geometry(f"{width}x{height}")

def visual_grid(parent, rows: int, cols: int):
    """Provide a visual representation of how the grid is laid out."""
    for y in range(rows):
        for x in range(cols):
            label = tk.Label(parent)
            label.config(text = f"({y},{x})", borderwidth = 1, relief = "solid")
            label.grid(row = y, column = x, sticky = "nsew")