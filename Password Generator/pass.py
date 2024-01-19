import tkinter as tk
from tkinter import ttk
import string
import random

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            result.set("Please enter a positive length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result.set(f"Generated Password: {password}")

    except ValueError:
        result.set("Invalid input. Please enter a valid integer for the length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Styling
window.geometry("400x200")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Header label
header_label = ttk.Label(window, text="Password Generator", font=("Helvetica", 18), background="#f0f0f0")
header_label.grid(row=0, column=0, padx=10, pady=10)

# Entry widget for password length
entry_length = ttk.Entry(window, width=15, font=("Helvetica", 12))
entry_length.grid(row=1, column=0, padx=10, pady=10)

# Button to generate password
generate_button = ttk.Button(window, text="Generate Password", command=generate_password, style="TButton")
generate_button.grid(row=2, column=0, padx=10, pady=10)

# Result label
result = tk.StringVar()
result_label = ttk.Label(window, textvariable=result, font=("Helvetica", 12), background="#f0f0f0")
result_label.grid(row=3, column=0, padx=10, pady=10)

# Styling for the button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))

# Run the main loop
window.mainloop()
