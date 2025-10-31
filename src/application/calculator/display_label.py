from tkinter import Label, Frame

class DisplayLabel(Label):
    _instance = None

    # Ensure only one instance exist
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DisplayLabel, cls).__new__(cls)

        return cls._instance
    
    def __init__(self, parent: Frame):
        Label.__init__(self, parent)

    def add(self, char: str):
        text: str = self.cget("text")

        if char == "0" and not text:
            return

        if text and text[-1].isdigit() and char == "(":
            new_text = text + "*" + char

        else:
            new_text = text + char

        self.config(text = new_text)

    def add_decimal(self):
        text = self.cget("text")

        if "." not in text:
            new_text = self.cget("text") + "."
            self.config(text = new_text)

    def delete(self):
        new_text = self.cget("text")[: -1]

        self.config(text = new_text)

    def clear(self):
        self.config(text = "")