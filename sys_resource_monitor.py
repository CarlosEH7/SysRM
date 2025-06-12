import tkinter as tk
from tkinter import ttk
import psutil

root = tk.Tk()
root.title("System Resource Monitor")
root.geometry("300x150")

cpu_label = ttk.Label(root, text="CPU Usage: ", font=("Helvetica", 12) )
cpu_label.pack(pady=10)

memory_label = ttk.Label(root, text="Memory Usage: ", font=("Helvetica", 12))
memory_label.pack(pady=10)

def update_info():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
    memory_label.config(text=f"Memory Usage: {memory_percent}%")

    root.after(1000, update_info)

update_info()
root.mainloop()
