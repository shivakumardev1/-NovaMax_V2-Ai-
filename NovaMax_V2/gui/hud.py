import tkinter as tk
from tkinter import ttk

class NovaHUD:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NovaMax V2")
        self.root.geometry("430x260")
        self.root.configure(bg="#080b12")
        self.status = tk.StringVar(value="STANDBY")

        title = tk.Label(
            self.root, text="NOVA MAX", font=("Segoe UI", 24, "bold"),
            fg="#7dd3fc", bg="#080b12"
        )
        title.pack(pady=(35, 8))

        label = tk.Label(
            self.root, textvariable=self.status, font=("Segoe UI", 13),
            fg="white", bg="#080b12"
        )
        label.pack()

        self.bar = ttk.Progressbar(self.root, mode="indeterminate", length=260)
        self.bar.pack(pady=25)

    def set_status(self, value):
        self.status.set(value)

    def start(self):
        self.root.mainloop()
