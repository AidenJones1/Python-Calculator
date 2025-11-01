from tkinter import Label, Frame
from enum import Enum

class Mode(Enum):
    Display = 1,
    Entry = 2

class DisplayLabel(Label):
    _instance = None

    # Ensure only one instance exist
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DisplayLabel, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, parent: Frame):
        Label.__init__(self, parent)

        self.previous_answer = "0"
        self.mode = Mode.Entry

    # Display Editting
    def add(self, char: str):
        """Adds the character to the display."""
        if self.mode == Mode.Entry:
            text: str = self.cget("text")

            if char == "0" and not text:
                return

            if text and text[-1].isdigit() and char == "(":
                new_text = text + "*" + char

            else:
                new_text = text + char

            self.config(text = new_text)

    def delete(self):
        """Removes the most recent character from the display."""
        if self.mode == Mode.Entry:
            new_text = self.cget("text")[: -1]

            # Prevents user from having a '0' by itself
            if new_text == "0":
                new_text = ""

            self.config(text = new_text)

        elif self.mode == Mode.Display:
            self.clear()

    def clear(self):
        """Reset the display."""
        self.config(text = "")

        if self.mode == Mode.Display:
            self.mode = Mode.Entry
    
    def set_display(self, new_text):
        """Set the display to some string."""
        self.config(text = new_text)
        self.mode = Mode.Display

    # Display
    def get_expression(self) -> str:
        """Retrieve whatever is stored in the display."""
        return self.cget("text")

    # Previous Answer
    def set_previous_answer(self, new_ans):
        """Set the previous answer."""
        self.previous_answer = new_ans

    def display_previous_answer(self):
        """Put whatever is stored in the previous answer on the display."""
        self.config(text = self.previous_answer)
        self.mode = Mode.Display

    # Display Mode
    def in_entry_mode(self):
        """Check if the display is in Display Mode"""
        return self.mode == Mode.Entry