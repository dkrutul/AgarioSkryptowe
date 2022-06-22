import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="Test",prompt="What's your Name?:")
