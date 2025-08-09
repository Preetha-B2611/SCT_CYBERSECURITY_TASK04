"""
Safe Keylogger Simulation
-------------------------
Logs keystrokes typed into this program's window only (not system-wide).
Author: Your Name
License: MIT
"""

import tkinter as tk
from datetime import datetime

LOGFILE = "typed_log.txt"

def log_key(event):
    """Logs each key pressed inside the program window."""
    ts = datetime.utcnow().isoformat() + "Z"
    entry = f"{ts}\t{event.keysym}\t{repr(event.char)}\n"
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(entry)

def on_submit():
    """Optional: save the full text box content."""
    ts = datetime.utcnow().isoformat() + "Z"
    content = text.get("1.0", tk.END).rstrip()
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts}\tSUBMIT\t{repr(content)}\n")
    status_label.config(text=f"Saved at {ts}")

root = tk.Tk()
root.title("Safe Keylogger Simulation")

frame = tk.Frame(root, padx=12, pady=12)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Type here (only this window will be logged):")
label.pack(anchor="w")

text = tk.Text(frame, width=60, height=12)
text.pack(fill="both", expand=True)
text.focus_set()
text.bind("<Key>", log_key)

btn = tk.Button(frame, text="Save/Submit", command=on_submit)
btn.pack(pady=(8,0))

status_label = tk.Label(frame, text="Log file: " + LOGFILE)
status_label.pack(anchor="w", pady=(6,0))

root.mainloop()
