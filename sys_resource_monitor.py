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