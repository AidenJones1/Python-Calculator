import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # Pyinstaller bundle
    except:
        base_path = os.path.abspath(".") # Dev Env
    
    return os.path.join(base_path, relative_path)