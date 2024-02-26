import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
digits = "0123456789"
symbols = "()[]{},./\\+*#!@#$%^&*_-?:;"

up, low, dig, sym = True, True, True, True

key = ""
if up:
    key += upper_case
if low:
    key += lower_case
if dig:
    key += digits
if sym:
    key += symbols

def generate_password(length):
    password = "".join(random.sample(key, length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return
        password = generate_password(length)
        password_label.config(text="Generated password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the length.")

# Create Tkinter window
root = tk.Tk()
root.title("Password Generator")
icon_image=PhotoImage(file="421648.png")
root.iconphoto(False,icon_image)

# Add style
style = ttk.Style()
style.configure('TButton', font=('calibri', 12, 'bold'), borderwidth='4')
style.configure('TLabel', font=('calibri', 12), foreground='blue')
style.configure('TEntry', font=('calibri', 12), borderwidth='2')

# Create widgets
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, padx=20, pady=20)

length_label = ttk.Label(main_frame, text="Enter the desired length of the password:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
length_entry = ttk.Entry(main_frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
password_label = ttk.Label(main_frame, text="")
password_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
